# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

Always use the project-local virtual environment (`venv/`) — never install packages globally.

```powershell
# Create the venv (first time only)
python -m venv venv

# Install/update dependencies
.\venv\Scripts\pip.exe install -r requirements.txt

# Run the app
.\venv\Scripts\streamlit.exe run app.py

# Compile-check without running the UI
.\venv\Scripts\python.exe -m py_compile app.py
```

There are no automated tests, lint config, or CI in this repo. Streamlit re-executes `app.py` per browser session on each interaction, so an HTTP 200 from the server does not prove the script ran without error — verify data-fetching logic by exercising it directly (e.g. a standalone script hitting the same API calls) rather than relying on the server responding.

## Architecture

Single-file Streamlit app (`app.py`) — a weather dashboard backed entirely by the free [Open-Meteo](https://open-meteo.com) APIs, which require no API key:

- **Geocoding** (`geocode_city`) — resolves a city name to coordinates via the geocoding API; returns up to 5 matches so the UI can disambiguate same-named cities (e.g. multiple "Springfield"s) using `admin1`/`country`.
- **Forecast** (`fetch_weather`) — fetches `current`, `hourly`, and `daily` blocks in one call, parameterized by unit system and forecast length.
- **Air quality** (`fetch_air_quality`) — separate endpoint/host, fetched independently and only if the sidebar toggle is on.

All three fetch functions are wrapped in `st.cache_data` with different TTLs (weather 10 min, air quality 30 min, geocoding 1 hour) — cached by call arguments, so switching city/units/forecast-days naturally busts the cache. The sidebar's "Refresh data" button calls `st.cache_data.clear()` to force-bypass this.

State that must survive reruns (current city, recent-search list) lives in `st.session_state`, initialized once near the top of the file.

The page is a single top-to-bottom flow: sidebar controls → geocode → fetch weather → hero card (custom HTML/CSS) → metrics row → three tabs (Daily Forecast, Charts, Air Quality & Map). Custom styling is injected once via a `st.markdown(..., unsafe_allow_html=True)` `<style>` block near the top, with light/dark variants driven by `prefers-color-scheme`.

### Charts

Charts are built with `plotly.graph_objects` (not `plotly.express`) and follow fixed conventions rather than per-chart improvisation:
- Never combine two differently-scaled measures on one chart with dual y-axes — temperature, precipitation, and wind each get their own chart instead.
- Colors are pulled from fixed module-level constants (`BLUE`, `ORANGE`, `AQUA`, plus `GOOD`/`WARNING`/`SERIOUS`/`CRITICAL` for AQI status) rather than Plotly's default palette, and a given series/category always uses the same color (e.g. High is always `ORANGE`, Low is always `BLUE`).
- Every trace sets an explicit `hovertemplate`; multi-series charts (e.g. the High/Low trend) show a legend.

`WEATHER_CODES` maps WMO weather codes (from the API) to `(emoji, description)` — extend this dict if new codes need coverage, don't special-case codes elsewhere.
