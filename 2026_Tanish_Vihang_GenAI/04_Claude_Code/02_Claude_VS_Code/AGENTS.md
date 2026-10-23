# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Always use the project virtual environment (`.venv`) — activate it first (`.venv\Scripts\Activate.ps1` on Windows PowerShell) or call its Python directly.

```
pip install -r requirements.txt
python -m streamlit run app.py          # serves on http://localhost:8501
python -m streamlit run app.py --server.headless true --server.port 8501
```

There is no test suite, linter, or build step. No API key is needed (Open-Meteo is keyless); `.streamlit/secrets.toml` is a leftover from an old WeatherAPI version and is not referenced.

To check changes without a browser, use Streamlit's headless harness (`from streamlit.testing.v1 import AppTest; at = AppTest.from_file("app.py", default_timeout=60); at.session_state["dark_mode"] = True; at.run(); at.exception`). Widget keys you can preset: `city_input`, `units`, `forecast_days`, `history_days`, `dark_mode`. It hits the live API, so a transient network/rate-limit failure can hit the `st.stop()` path and yield zero tabs — rerun before assuming a code bug. `AppTest` has no `plotly_chart` accessor; assert on `at.tabs`, `at.metric`, `at.markdown`, `at.exception`.

## Architecture

The whole app is a single script, [app.py](app.py), executed top to bottom on every Streamlit rerun. Order matters:

1. `resolve_palette(dark)` returns one dict of colors used by both the injected CSS (as `--am-*` CSS custom properties) and every Plotly figure (`COLORS[...]`).
2. `st.session_state.setdefault(...)` for all persistent state, then `COLORS = resolve_palette(st.session_state["dark_mode"])`.
3. A dynamic `<style>:root{--am-*}` block (f-string, depends on theme) followed by a large static `<style>` block.
4. Helpers, three `@st.cache_data` fetchers (`geocode_city` 24h, `fetch_forecast` / `fetch_air_quality` 10 min), sidebar, location resolution, DataFrame construction, hero card, then five tabs (Overview, Temperature, Wind & UV, Air Quality, History) containing ~11 Plotly figures, and a forecast-table expander.

Data comes only from Open-Meteo: geocoding, forecast (one call uses `past_days` + `forecast_days` to get history and forecast together, then split into hourly/daily/forecast/today frames), and air quality. WMO weather codes are mapped to emoji/text via `WMO_TEXT` / `condition_icon`.

### Theming (non-obvious)

- Streamlit's native theme cannot be switched from Python. `.streamlit/config.toml` defines both `[theme.light]` and `[theme.dark]` (Apple-style), but the in-app sidebar toggle (`st.sidebar.toggle(..., key="dark_mode")`) works by re-injecting CSS and rebuilding Plotly colors from `session_state`.
- Native widget text (radio options, widget labels, captions, slider ticks/values, selectbox, text-input labels) keeps Streamlit's own color and is not affected by ancestor `color`, so it is overridden with `!important` rules scoped to specific `data-testid`s. Do not replace these with a blanket `*` rule — it breaks inline-colored elements and the primary button (which is explicitly forced to white).
- Streamlit 1.64 has no baseweb; select via `data-testid` (`stTabs`, `stTab`, `stRadioOption`, `stWidgetLabel`, `stCaptionContainer`, `stSliderTickBar`, ...) or ARIA attributes. Portal-rendered pieces (selectbox dropdown popover, slider thumb internals) may not follow the toggle.

### Chart rules

- One y-axis per chart (no dual-axis); use subplots or separate charts instead.
- Two or more series need a legend (`legend_row`); build layouts via `chart_layout(**overrides)` so grid/ink colors follow the theme.
- Categorical colors are blue and orange from the palette; status colors (good/warning/serious/critical) are mode-invariant; sequential data uses `BLUE_RAMP`.
- `add_vline` on a date axis needs `pd.Timestamp(...)`, not a `datetime.date`.
- Bars use `marker=dict(cornerradius=6)`; area fills use `rgba({COLORS['blue_rgb']}, alpha)`.
