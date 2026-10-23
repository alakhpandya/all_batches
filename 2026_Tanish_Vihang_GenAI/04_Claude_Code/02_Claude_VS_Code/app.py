"""
Weather Dashboard - Streamlit app powered by Open-Meteo (free, no API key required)

Run with:  streamlit run app.py

Data sources (all free, no key needed):
  - Geocoding:    https://open-meteo.com/en/docs/geocoding-api
  - Forecast:     https://open-meteo.com/en/docs (16-day forecast + up to 92 days history)
  - Air Quality:  https://open-meteo.com/en/docs/air-quality-api
"""

from datetime import date, datetime

import pandas as pd
import plotly.graph_objects as go
import requests
import streamlit as st

# --------------------------------------------------------------------------
# Palette (validated categorical + sequential + status colors, light/dark aware)
# --------------------------------------------------------------------------
# Sequential blue ramp (light -> dark), used for heatmap/wind-rose fills that
# sit inside their own cells (not against the card surface), so one ramp
# serves both modes.
BLUE_RAMP = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#2a78d6", "#1c5cab", "#104281", "#0d366b"]


def resolve_palette(dark: bool) -> dict:
    """Single source of truth for every color used in CSS and Plotly charts.

    Status colors (good/warning/serious/critical) and the muted axis gray are
    validated as mode-invariant; chart series and UI chrome swap to the
    validated dark-surface steps.
    """
    shared = {
        "good": "#0ca30c", "warning": "#fab219", "serious": "#ec835a", "critical": "#d03b3b",
        "muted": "#898781",
    }
    if dark:
        return {
            **shared,
            "blue": "#3987e5", "blue_rgb": "57,135,229",
            "orange": "#d95926",
            "text_secondary": "#c3c2b7",
            "grid": "#2c2c2a",
            "hover_bg": "#1a1a19", "hover_border": "rgba(255,255,255,0.10)", "hover_text": "#ffffff",
            "page_bg": "#000000", "secondary_bg": "#1c1c1e",
            "card": "#1a1a19", "chip": "#2c2c2e",
            "text": "#ffffff", "text_muted": "#98989d",
            "border": "rgba(255,255,255,0.08)",
            "shadow": "0 1px 2px rgba(0,0,0,0.3), 0 10px 24px rgba(0,0,0,0.35)",
        }
    return {
        **shared,
        "blue": "#2a78d6", "blue_rgb": "42,120,214",
        "orange": "#eb6834",
        "text_secondary": "#52514e",
        "grid": "#e1e0d9",
        "hover_bg": "#ffffff", "hover_border": "rgba(0,0,0,0.08)", "hover_text": "#1d1d1f",
        "page_bg": "#ffffff", "secondary_bg": "#f5f5f7",
        "card": "#ffffff", "chip": "#f5f5f7",
        "text": "#1d1d1f", "text_muted": "#86868b",
        "border": "rgba(0,0,0,0.06)",
        "shadow": "0 1px 2px rgba(0,0,0,0.04), 0 10px 24px rgba(0,0,0,0.06)",
    }


FONT_STACK = ('-apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", '
              '"Segoe UI", Helvetica, Arial, sans-serif')

BASE_URL_GEO = "https://geocoding-api.open-meteo.com/v1/search"
BASE_URL_FORECAST = "https://api.open-meteo.com/v1/forecast"
BASE_URL_AQ = "https://air-quality-api.open-meteo.com/v1/air-quality"

COMPASS = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
           "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]

WMO_TEXT = {
    0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Rime fog",
    51: "Light drizzle", 53: "Drizzle", 55: "Dense drizzle",
    56: "Freezing drizzle", 57: "Dense freezing drizzle",
    61: "Slight rain", 63: "Rain", 65: "Heavy rain",
    66: "Freezing rain", 67: "Heavy freezing rain",
    71: "Slight snow", 73: "Snow", 75: "Heavy snow", 77: "Snow grains",
    80: "Slight rain showers", 81: "Rain showers", 82: "Violent rain showers",
    85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Severe thunderstorm with hail",
}

WHO_GUIDELINE = {  # WHO 2021 air quality guideline levels, micrograms/m3
    "pm2_5": ("PM2.5", 15),
    "pm10": ("PM10", 45),
    "nitrogen_dioxide": ("NO₂", 25),
    "ozone": ("O₃", 100),
    "sulphur_dioxide": ("SO₂", 40),
    "carbon_monoxide": ("CO", 4000),
}

# --------------------------------------------------------------------------
# Page setup
# --------------------------------------------------------------------------
st.set_page_config(page_title="Weather Dashboard", page_icon="\U0001F324️", layout="wide")

st.session_state.setdefault("history", [])
st.session_state.setdefault("city_input", "London")
st.session_state.setdefault("units", "Metric (°C, km/h)")
st.session_state.setdefault("forecast_days", 7)
st.session_state.setdefault("history_days", 14)
st.session_state.setdefault("pending_location", None)
st.session_state.setdefault("dark_mode", False)

COLORS = resolve_palette(st.session_state["dark_mode"])

# CSS custom properties resolved from the active mode (small f-string block).
st.markdown(
    f"""
    <style>
    :root {{
        --am-card: {COLORS['card']};
        --am-chip: {COLORS['chip']};
        --am-text: {COLORS['text']};
        --am-text-secondary: {COLORS['text_secondary']};
        --am-text-muted: {COLORS['text_muted']};
        --am-border: {COLORS['border']};
        --am-shadow: {COLORS['shadow']};
        --am-page-bg: {COLORS['page_bg']};
        --am-secondary-bg: {COLORS['secondary_bg']};
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Static design system, driven entirely by the CSS vars set above.
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
                     "Segoe UI", Helvetica, Arial, sans-serif !important;
    }
    h1, h2, h3 {
        font-weight: 600 !important;
        letter-spacing: -0.02em;
    }
    hr, [data-testid="stDivider"] { border-color: var(--am-border) !important; }

    /* Native chrome follows the in-app toggle, not just Streamlit's own theme */
    [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: var(--am-page-bg) !important;
        color: var(--am-text);
    }
    [data-testid="stHeader"], [data-testid="stAppHeader"], [data-testid="stToolbar"] {
        background-color: transparent !important;
    }
    [data-testid="stSidebar"], [data-testid="stSidebarContent"] {
        background-color: var(--am-secondary-bg) !important;
        color: var(--am-text);
    }
    [data-testid="stTextInput"] input, [data-testid="stNumberInput"] input,
    textarea, select {
        background-color: var(--am-chip) !important;
        color: var(--am-text) !important;
        border-color: var(--am-border) !important;
    }
    .stButton button:not([kind="primary"]), [data-testid="stButton"] button:not([kind="primary"]) {
        background-color: var(--am-chip);
        color: var(--am-text) !important;
        border: 1px solid var(--am-border);
    }
    .stButton button[kind="primary"], [data-testid="stButton"] button[kind="primary"] {
        background-color: #0A84FF !important;
        color: #ffffff !important;
        border: none !important;
    }

    /* Native widget text: these components set their own text color from
       Streamlit's OWN theme resolution, which the in-app toggle doesn't
       control, so they need an explicit (and !important) override here. */
    [data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] * {
        color: var(--am-text-secondary) !important;
    }
    [data-testid="stRadioOption"], [data-testid="stRadioOption"] * {
        color: var(--am-text) !important;
    }
    [data-testid="stCaptionContainer"], [data-testid="stCaptionContainer"] * {
        color: var(--am-text-muted) !important;
    }
    [data-testid="stSliderTickBar"], [data-testid="stSliderThumbValue"],
    [data-testid="stSliderTickBar"] *, [data-testid="stSliderThumbValue"] * {
        color: var(--am-text-secondary) !important;
    }
    [data-testid="stSelectbox"] *, [data-testid="stTextInput"] label,
    [data-testid="stTextInput"] label * {
        color: var(--am-text) !important;
    }

    [data-testid="stDataFrame"], [data-testid="stExpander"] {
        background: var(--am-card);
        border: 1px solid var(--am-border);
        border-radius: 16px !important;
        overflow: hidden;
    }

    /* Hero current-conditions card */
    .hero-card {
        background: var(--am-card);
        border: 1px solid var(--am-border);
        border-radius: 28px;
        padding: 28px 32px;
        box-shadow: var(--am-shadow);
        margin-bottom: 6px;
    }
    .hero-eyebrow {
        font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em;
        text-transform: uppercase; color: var(--am-text-muted);
    }
    .hero-place { font-size: 1.55rem; font-weight: 600; color: var(--am-text); margin-top: 2px; }
    .hero-time { font-size: 0.85rem; color: var(--am-text-secondary); margin-top: 2px; }
    .hero-main { display: flex; align-items: center; gap: 22px; margin-top: 18px; flex-wrap: wrap; }
    .hero-icon { font-size: 60px; line-height: 1; }
    .hero-temp { font-size: 84px; font-weight: 200; letter-spacing: -0.03em; line-height: 1; color: var(--am-text); }
    .hero-temp .unit { font-size: 32px; font-weight: 300; }
    .hero-meta { min-width: 160px; }
    .hero-condition { font-size: 1.1rem; font-weight: 500; color: var(--am-text); }
    .hero-feels { font-size: 0.9rem; color: var(--am-text-secondary); margin-top: 2px; }

    .detail-grid {
        display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
        gap: 10px; margin-top: 22px;
    }
    .detail-chip { background: var(--am-chip); border-radius: 16px; padding: 12px 14px; }
    .detail-label {
        font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;
        color: var(--am-text-muted);
    }
    .detail-value { font-size: 1.25rem; font-weight: 600; color: var(--am-text); margin-top: 3px; }
    .detail-sub { font-size: 0.74rem; color: var(--am-text-secondary); margin-top: 1px; }

    /* Forecast day cards */
    .day-card {
        background: var(--am-card); border: 1px solid var(--am-border); border-radius: 20px;
        padding: 16px 8px; text-align: center; box-shadow: var(--am-shadow);
    }
    .day-card .day-label { font-size: 0.78rem; font-weight: 600; color: var(--am-text-secondary); }
    .day-card .day-icon { font-size: 30px; margin: 6px 0; }
    .day-card .day-temps { font-size: 1.05rem; font-weight: 600; color: var(--am-text); }
    .day-card .day-low { color: var(--am-text-muted); font-weight: 500; margin-left: 4px; }
    .day-card .day-sub { font-size: 0.72rem; color: var(--am-text-muted); margin-top: 2px; }

    .status-badge {
        display: inline-block; padding: 4px 12px; border-radius: 999px;
        color: white; font-weight: 600; font-size: 0.8rem;
    }
    .legend-row { display: flex; gap: 16px; flex-wrap: wrap; margin-top: 8px; }
    .legend-dot { display: inline-flex; align-items: center; gap: 6px; font-size: 0.78rem; color: var(--am-text-secondary); }
    .legend-dot span.sw { width: 9px; height: 9px; border-radius: 3px; display: inline-block; }

    .section-label { font-size: 0.98rem; font-weight: 600; color: var(--am-text); margin: 4px 0 10px 0; }

    /* Chart cards */
    [data-testid="stPlotlyChart"] {
        background: var(--am-card);
        border: 1px solid var(--am-border);
        border-radius: 20px;
        padding: 12px 8px 4px 8px;
        box-shadow: var(--am-shadow);
    }

    /* Tabs -> segmented control */
    [data-testid="stTabs"] [role="tablist"] {
        gap: 4px; background: var(--am-chip); padding: 4px; border-radius: 980px;
        width: fit-content; border-bottom: none !important;
    }
    [data-testid="stTab"] {
        border-radius: 980px !important; padding: 6px 18px !important; font-weight: 500 !important;
        color: var(--am-text-secondary);
    }
    [data-testid="stTab"][aria-selected="true"] {
        background: var(--am-card) !important; box-shadow: 0 1px 4px rgba(0,0,0,0.12);
        color: var(--am-text) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------


def condition_icon(code: int, is_day: int = 1) -> str:
    if code in (0, 1):
        return "☀️" if is_day else "\U0001F319"
    if code == 2:
        return "⛅" if is_day else "☁️"
    if code == 3:
        return "☁️"
    if code in (45, 48):
        return "\U0001F32B️"
    if code in (51, 53, 55, 56, 57):
        return "\U0001F326️"
    if code in (61, 63, 65, 66, 67, 80, 81, 82):
        return "\U0001F327️"
    if code in (71, 73, 75, 77, 85, 86):
        return "\U0001F328️"
    if code in (95, 96, 99):
        return "⛈️"
    return "\U0001F321️"


def compass_dir(deg: float) -> str:
    return COMPASS[round(deg / 22.5) % 16]


def us_aqi_category(v: float):
    if v <= 50:
        return "Good", COLORS["good"]
    if v <= 100:
        return "Moderate", COLORS["warning"]
    if v <= 150:
        return "Unhealthy (sensitive)", COLORS["serious"]
    if v <= 200:
        return "Unhealthy", COLORS["critical"]
    if v <= 300:
        return "Very Unhealthy", COLORS["critical"]
    return "Hazardous", COLORS["critical"]


def uv_category(v: float):
    if v < 3:
        return "Low", COLORS["good"]
    if v < 6:
        return "Moderate", COLORS["warning"]
    if v < 8:
        return "High", COLORS["serious"]
    if v < 11:
        return "Very High", COLORS["critical"]
    return "Extreme", COLORS["critical"]


def guideline_category(pct: float):
    if pct <= 100:
        return COLORS["good"]
    if pct <= 200:
        return COLORS["warning"]
    if pct <= 300:
        return COLORS["serious"]
    return COLORS["critical"]


def legend_row(items: list[tuple[str, str]]) -> None:
    dots = "".join(
        f'<span class="legend-dot"><span class="sw" style="background:{color}"></span>{label}</span>'
        for label, color in items
    )
    st.markdown(f'<div class="legend-row">{dots}</div>', unsafe_allow_html=True)


def section_label(text: str) -> None:
    st.markdown(f'<div class="section-label">{text}</div>', unsafe_allow_html=True)


def chart_layout(**overrides) -> dict:
    """Shared Plotly layout: Apple-system font, transparent surface, soft tooltip."""
    layout = dict(
        font=dict(family=FONT_STACK, size=12, color=COLORS["text_secondary"]),
        margin=dict(l=8, r=8, t=8, b=8),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        hoverlabel=dict(
            bgcolor=COLORS["hover_bg"],
            bordercolor=COLORS["hover_border"],
            font=dict(family=FONT_STACK, size=12, color=COLORS["hover_text"]),
        ),
    )
    layout.update(overrides)
    return layout


# Horizontal legend pinned above the plot area, top-right.
TOP_LEGEND = dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)


def grid_axis(title: str) -> dict:
    return dict(showgrid=True, gridcolor=COLORS["grid"], title=title)


def time_frame(block: dict, key: str, parse) -> pd.DataFrame:
    """Turn an Open-Meteo column block into a DataFrame, parsing "time" into column `key`."""
    return pd.DataFrame({key: [parse(t) for t in block["time"]],
                         **{k: v for k, v in block.items() if k != "time"}})


def push_history(loc: dict) -> None:
    hist = [h for h in st.session_state["history"] if h["label"] != loc["label"]]
    hist.insert(0, loc)
    st.session_state["history"] = hist[:8]


@st.cache_data(ttl=86400, show_spinner=False)
def geocode_city(name: str) -> list[dict]:
    resp = requests.get(
        BASE_URL_GEO, params={"name": name, "count": 6, "language": "en", "format": "json"}, timeout=10
    )
    resp.raise_for_status()
    return resp.json().get("results") or []


def get_json(url: str, params: dict) -> dict:
    resp = requests.get(url, params=params, timeout=15)
    payload = resp.json()
    if resp.status_code != 200:
        raise RuntimeError(payload.get("reason", "Unknown error"))
    return payload


@st.cache_data(ttl=600, show_spinner=False)
def fetch_forecast(lat: float, lon: float, temp_unit: str, wind_unit: str,
                    precip_unit: str, forecast_days: int, past_days: int) -> dict:
    params = {
        "latitude": lat, "longitude": lon, "timezone": "auto",
        "temperature_unit": temp_unit, "wind_speed_unit": wind_unit, "precipitation_unit": precip_unit,
        "forecast_days": forecast_days, "past_days": past_days,
        "current": ",".join([
            "temperature_2m", "relative_humidity_2m", "apparent_temperature", "is_day",
            "precipitation", "weather_code", "pressure_msl", "cloud_cover",
            "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m",
        ]),
        "hourly": ",".join([
            "temperature_2m", "apparent_temperature", "precipitation_probability", "precipitation",
            "weather_code", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", "uv_index",
        ]),
        "daily": ",".join([
            "weather_code", "temperature_2m_max", "temperature_2m_min",
            "sunrise", "sunset", "daylight_duration", "uv_index_max",
            "precipitation_sum", "precipitation_probability_max",
        ]),
    }
    return get_json(BASE_URL_FORECAST, params)


@st.cache_data(ttl=600, show_spinner=False)
def fetch_air_quality(lat: float, lon: float) -> dict:
    params = {
        "latitude": lat, "longitude": lon, "timezone": "auto",
        "hourly": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,sulphur_dioxide,ozone,us_aqi",
        "forecast_days": 3,
    }
    return get_json(BASE_URL_AQ, params)


# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------
st.sidebar.title("\U0001F324️ Weather Dashboard")
st.sidebar.toggle("🌙 Dark Mode", key="dark_mode")

city = st.sidebar.text_input("City", key="city_input")
st.sidebar.button("Search", type="primary", width="stretch")

units_choice = st.sidebar.radio("Units", ["Metric (°C, km/h)", "Imperial (°F, mph)"], key="units")
metric = units_choice.startswith("Metric")
temp_unit = "celsius" if metric else "fahrenheit"
wind_unit = "kmh" if metric else "mph"
precip_unit = "mm" if metric else "inch"
temp_symbol = "°C" if metric else "°F"
wind_label = "km/h" if metric else "mph"

forecast_days = st.sidebar.slider("Forecast horizon (days)", 3, 14, key="forecast_days")
history_days = st.sidebar.slider("History window (days)", 7, 30, key="history_days")

if st.session_state["history"]:
    st.sidebar.caption("Recent searches")
    for item in st.session_state["history"]:
        if st.sidebar.button(item["label"], key=f"hist_{item['label']}", width="stretch"):
            st.session_state["pending_location"] = item
            st.session_state["city_input"] = item["label"]
            st.rerun()

st.sidebar.divider()
st.sidebar.caption("Data by [Open-Meteo](https://open-meteo.com/) — free, no API key required.")

# --------------------------------------------------------------------------
# Resolve location
# --------------------------------------------------------------------------
st.title("Weather Dashboard")

location = None
if st.session_state["pending_location"] is not None:
    location = st.session_state["pending_location"]
    st.session_state["pending_location"] = None
elif city.strip():
    try:
        with st.spinner(f"Locating {city}..."):
            results = geocode_city(city.strip())
    except requests.RequestException as exc:
        st.error(f"Network error while looking up '{city}': {exc}")
        st.stop()

    if not results:
        st.error(f"No location found for '{city}'.")
        st.stop()

    if len(results) == 1:
        chosen = results[0]
    else:
        options = {
            ", ".join(b for b in [r["name"], r.get("admin1", ""), r["country"]] if b): r
            for r in results
        }
        pick = st.sidebar.selectbox("Multiple matches — pick one", list(options))
        chosen = options[pick]

    location = {
        "label": ", ".join(b for b in [chosen["name"], chosen.get("country", "")] if b),
        "name": chosen["name"],
        "country": chosen.get("country", ""),
        "admin1": chosen.get("admin1", ""),
        "lat": chosen["latitude"],
        "lon": chosen["longitude"],
    }
else:
    st.info("Enter a city in the sidebar to see the forecast.")
    st.stop()

push_history(location)

# --------------------------------------------------------------------------
# Fetch data
# --------------------------------------------------------------------------
try:
    with st.spinner(f"Fetching weather for {location['name']}..."):
        forecast = fetch_forecast(
            location["lat"], location["lon"], temp_unit, wind_unit, precip_unit,
            forecast_days, history_days,
        )
        air_quality = fetch_air_quality(location["lat"], location["lon"])
except RuntimeError as exc:
    st.error(f"Could not fetch weather: {exc}")
    st.stop()
except requests.RequestException as exc:
    st.error(f"Network error while contacting Open-Meteo: {exc}")
    st.stop()

current = forecast["current"]
hourly_df = time_frame(forecast["hourly"], "time", datetime.fromisoformat)
daily_df = time_frame(forecast["daily"], "date", date.fromisoformat)
aq_df = time_frame(air_quality["hourly"], "time", datetime.fromisoformat)

now = datetime.fromisoformat(current["time"])
today_date = now.date()

forecast_daily_df = daily_df[daily_df["date"] >= today_date].reset_index(drop=True)
today_hourly_df = hourly_df[hourly_df["time"].dt.date == today_date].reset_index(drop=True)
forecast_hourly_df = hourly_df[hourly_df["time"].dt.date >= today_date].reset_index(drop=True)

current_aq = aq_df.loc[(aq_df["time"] - now).abs().idxmin()]
current_uv = hourly_df.loc[(hourly_df["time"] - now).abs().idxmin(), "uv_index"]

# --------------------------------------------------------------------------
# Current conditions hero card
# --------------------------------------------------------------------------
place = ", ".join(b for b in [location["name"], location["admin1"] or location["country"]] if b)
icon = condition_icon(int(current["weather_code"]), int(current["is_day"]))
condition_text = WMO_TEXT.get(int(current["weather_code"]), "Unknown")
aqi_label, aqi_color = us_aqi_category(current_aq["us_aqi"])
uv_label, uv_color = uv_category(current_uv)

st.markdown(
    f"""
    <div class="hero-card">
        <div class="hero-eyebrow">Current Weather</div>
        <div class="hero-place">{place}</div>
        <div class="hero-time">{now.strftime('%A, %b %d · %H:%M')} local time
            &nbsp;·&nbsp; {location['lat']:.2f}, {location['lon']:.2f}</div>
        <div class="hero-main">
            <div class="hero-icon">{icon}</div>
            <div class="hero-temp">{current['temperature_2m']:.0f}<span class="unit">{temp_symbol}</span></div>
            <div class="hero-meta">
                <div class="hero-condition">{condition_text}</div>
                <div class="hero-feels">Feels like {current['apparent_temperature']:.0f}{temp_symbol}</div>
            </div>
        </div>
        <div class="detail-grid">
            <div class="detail-chip">
                <div class="detail-label">💧 Humidity</div>
                <div class="detail-value">{current['relative_humidity_2m']}%</div>
            </div>
            <div class="detail-chip">
                <div class="detail-label">💨 Wind</div>
                <div class="detail-value">{current['wind_speed_10m']:.0f} {wind_label}</div>
                <div class="detail-sub">{compass_dir(current['wind_direction_10m'])}</div>
            </div>
            <div class="detail-chip">
                <div class="detail-label">🌡️ Pressure</div>
                <div class="detail-value">{current['pressure_msl']:.0f}</div>
                <div class="detail-sub">mb</div>
            </div>
            <div class="detail-chip">
                <div class="detail-label">☀️ UV Index</div>
                <div class="detail-value">{current_uv:.1f}</div>
                <div class="detail-sub" style="color:{uv_color}; font-weight:600;">{uv_label}</div>
            </div>
            <div class="detail-chip">
                <div class="detail-label">🍃 Air Quality</div>
                <div class="detail-value">{current_aq['us_aqi']:.0f}</div>
                <div class="detail-sub" style="color:{aqi_color}; font-weight:600;">{aqi_label}</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

# --------------------------------------------------------------------------
# Tabs
# --------------------------------------------------------------------------
tab_overview, tab_temp, tab_wind, tab_air, tab_history = st.tabs(
    ["Overview", "Temperature", "Wind & UV", "Air Quality", "History"]
)

# --- Overview --------------------------------------------------------------
with tab_overview:
    section_label(f"{len(forecast_daily_df)}-day forecast")
    cards = forecast_daily_df.to_dict("records")
    for row_start in range(0, len(cards), 7):
        chunk = cards[row_start:row_start + 7]
        cols = st.columns(len(chunk))
        for col, d in zip(cols, chunk):
            date_label = d["date"].strftime("%a, %b %d")
            d_icon = condition_icon(int(d["weather_code"]))
            d_text = WMO_TEXT.get(int(d["weather_code"]), "")
            with col:
                st.markdown(
                    f"""
                    <div class="day-card">
                        <div class="day-label">{date_label}</div>
                        <div class="day-icon">{d_icon}</div>
                        <div class="day-temps">{d['temperature_2m_max']:.0f}{temp_symbol}
                            <span class="day-low">{d['temperature_2m_min']:.0f}{temp_symbol}</span></div>
                        <div class="day-sub">{d_text}</div>
                        <div class="day-sub">💧 {d['precipitation_probability_max']:.0f}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    st.write("")
    section_label("Today's hourly temperature vs. feels-like")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=today_hourly_df["time"], y=today_hourly_df["temperature_2m"],
        mode="lines", name="Temperature",
        line=dict(color=COLORS["blue"], width=2.5, shape="spline"),
        fill="tozeroy", fillcolor=f"rgba({COLORS['blue_rgb']},0.08)",
        hovertemplate="%{x|%H:%M}<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig.add_trace(go.Scatter(
        x=today_hourly_df["time"], y=today_hourly_df["apparent_temperature"],
        mode="lines", name="Feels like",
        line=dict(color=COLORS["orange"], width=2, dash="dot"),
        hovertemplate="%{x|%H:%M}<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig.update_layout(**chart_layout(
        height=340,
        legend=TOP_LEGEND,
        xaxis=dict(showgrid=False, tickformat="%H:%M"),
        yaxis=grid_axis(temp_symbol),
        hovermode="x unified",
    ))
    st.plotly_chart(fig, width="stretch")

# --- Temperature -------------------------------------------------------
with tab_temp:
    day_labels = [d.strftime("%a %m/%d") for d in forecast_daily_df["date"]]
    c1, c2 = st.columns(2)
    with c1:
        section_label("Daily high / low")
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=day_labels, y=forecast_daily_df["temperature_2m_max"], name="High",
            marker=dict(color=COLORS["blue"], cornerradius=6),
            hovertemplate="%{x} high<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
        ))
        fig2.add_trace(go.Bar(
            x=day_labels, y=forecast_daily_df["temperature_2m_min"], name="Low",
            marker=dict(color=COLORS["orange"], cornerradius=6),
            hovertemplate="%{x} low<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
        ))
        fig2.update_layout(**chart_layout(
            height=340, barmode="group",
            legend=TOP_LEGEND,
            xaxis=dict(showgrid=False),
            yaxis=grid_axis(temp_symbol),
        ))
        st.plotly_chart(fig2, width="stretch")

    with c2:
        section_label("Daily precipitation")
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=day_labels, y=forecast_daily_df["precipitation_sum"],
            marker=dict(color=COLORS["blue"], cornerradius=6), name="Precipitation",
            hovertemplate="%{x}<br>%{y:.1f} " + precip_unit + "<extra></extra>",
        ))
        fig3.update_layout(**chart_layout(
            height=340, showlegend=False,
            xaxis=dict(showgrid=False),
            yaxis=grid_axis(precip_unit),
        ))
        st.plotly_chart(fig3, width="stretch")

    section_label("Hour-by-hour temperature across the forecast")
    pivot = forecast_hourly_df.pivot_table(
        index=forecast_hourly_df["time"].dt.hour,
        columns=forecast_hourly_df["time"].dt.date,
        values="temperature_2m",
    )
    heat_colorscale = [
        [0.0, BLUE_RAMP[0]], [0.25, BLUE_RAMP[2]], [0.5, BLUE_RAMP[4]],
        [0.75, BLUE_RAMP[6]], [1.0, BLUE_RAMP[7]],
    ]
    fig4 = go.Figure(go.Heatmap(
        z=pivot.values,
        x=[d.strftime("%a %m/%d") for d in pivot.columns],
        y=[f"{h:02d}:00" for h in pivot.index],
        colorscale=heat_colorscale,
        colorbar=dict(title=temp_symbol, outlinewidth=0),
        hovertemplate="%{x}<br>%{y}<br>%{z:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig4.update_layout(**chart_layout(
        height=420,
        yaxis=dict(autorange="reversed"),
    ))
    st.plotly_chart(fig4, width="stretch")

# --- Wind & UV -----------------------------------------------------------
with tab_wind:
    chart_days = min(3, forecast_days)
    window_end = now.replace(hour=0, minute=0, second=0, microsecond=0) + pd.Timedelta(days=chart_days)
    chart_window = forecast_hourly_df[forecast_hourly_df["time"] < window_end]

    c1, c2 = st.columns(2)
    with c1:
        section_label(f"Wind speed & gusts (next {chart_days} days)")
        fig5 = go.Figure()
        fig5.add_trace(go.Scatter(
            x=chart_window["time"], y=chart_window["wind_speed_10m"], mode="lines",
            name="Speed", line=dict(color=COLORS["blue"], width=2.5),
            hovertemplate="%{x|%a %H:%M}<br>%{y:.0f} " + wind_label + "<extra></extra>",
        ))
        fig5.add_trace(go.Scatter(
            x=chart_window["time"], y=chart_window["wind_gusts_10m"], mode="lines",
            name="Gusts", line=dict(color=COLORS["orange"], width=2, dash="dot"),
            hovertemplate="%{x|%a %H:%M}<br>%{y:.0f} " + wind_label + "<extra></extra>",
        ))
        fig5.update_layout(**chart_layout(
            height=360,
            legend=TOP_LEGEND,
            xaxis=dict(showgrid=False),
            yaxis=grid_axis(wind_label),
            hovermode="x unified",
        ))
        st.plotly_chart(fig5, width="stretch")

    with c2:
        section_label("Wind rose — direction & speed frequency")
        if metric:
            edges = [0, 10, 20, 30, 40, float("inf")]
            bin_labels = ["0–10", "10–20", "20–30", "30–40", "40+"]
        else:
            edges = [0, 6, 12, 19, 25, float("inf")]
            bin_labels = ["0–6", "6–12", "12–19", "19–25", "25+"]

        wdf = forecast_hourly_df[["wind_speed_10m", "wind_direction_10m"]].dropna().copy()
        wdf["compass"] = wdf["wind_direction_10m"].apply(compass_dir)
        wdf["speed_bin"] = pd.cut(wdf["wind_speed_10m"], bins=edges, labels=bin_labels, right=False)
        pivot_wind = wdf.groupby(["compass", "speed_bin"], observed=True).size().unstack(fill_value=0)
        pivot_wind = pivot_wind.reindex(COMPASS, fill_value=0)

        ramp_idx = [1, 3, 4, 5, 7]
        fig6 = go.Figure()
        for i, label in enumerate(bin_labels):
            if label not in pivot_wind.columns:
                continue
            fig6.add_trace(go.Barpolar(
                r=pivot_wind[label].values, theta=COMPASS, name=f"{label} {wind_label}",
                marker_color=BLUE_RAMP[ramp_idx[i]],
                hovertemplate="%{theta}<br>" + label + " " + wind_label + "<br>%{r} hrs<extra></extra>",
            ))
        fig6.update_layout(**chart_layout(
            height=360,
            legend=dict(orientation="h", yanchor="bottom", y=-0.15, xanchor="center", x=0.5),
            polar=dict(
                radialaxis=dict(showgrid=True, gridcolor=COLORS["grid"]),
                angularaxis=dict(direction="clockwise", rotation=90),
                bgcolor="rgba(0,0,0,0)",
            ),
        ))
        st.plotly_chart(fig6, width="stretch")

    section_label(f"UV index (next {chart_days} days)")
    fig7 = go.Figure()
    max_uv = max(float(chart_window["uv_index"].max() or 0), 11) + 1
    bands = [(0, 3, COLORS["good"]), (3, 6, COLORS["warning"]),
             (6, 8, COLORS["serious"]), (8, max_uv, COLORS["critical"])]
    for y0, y1, color in bands:
        fig7.add_hrect(y0=y0, y1=y1, fillcolor=color, opacity=0.10, line_width=0, layer="below")
    fig7.add_trace(go.Scatter(
        x=chart_window["time"], y=chart_window["uv_index"], mode="lines",
        line=dict(color=COLORS["blue"], width=2.5, shape="spline"),
        fill="tozeroy", fillcolor=f"rgba({COLORS['blue_rgb']},0.15)", showlegend=False,
        hovertemplate="%{x|%a %H:%M}<br>UV %{y:.1f}<extra></extra>",
    ))
    fig7.update_layout(**chart_layout(
        height=300,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False, title="UV Index", range=[0, max_uv]),
    ))
    st.plotly_chart(fig7, width="stretch")
    legend_row([("Low", COLORS["good"]), ("Moderate", COLORS["warning"]),
                ("High", COLORS["serious"]), ("Very High / Extreme", COLORS["critical"])])

# --- Air Quality -----------------------------------------------------------
with tab_air:
    c1, c2 = st.columns([2, 3])
    with c1:
        section_label("Pollutants vs. WHO 24h guideline")
        # (label, % of guideline), worst pollutant first
        rows = sorted(
            ((label, current_aq[key] / guideline * 100) for key, (label, guideline) in WHO_GUIDELINE.items()),
            key=lambda r: r[1], reverse=True,
        )
        labels = [label for label, _ in rows]
        pcts = [pct for _, pct in rows]

        fig8 = go.Figure(go.Bar(
            x=pcts, y=labels, orientation="h",
            marker=dict(color=[guideline_category(p) for p in pcts], cornerradius=6),
            text=[f"{p:.0f}%" for p in pcts], textposition="outside",
            hovertemplate="%{y}: %{x:.0f}% of guideline<extra></extra>",
        ))
        fig8.add_vline(x=100, line_dash="dot", line_color=COLORS["text_secondary"],
                        annotation_text="guideline", annotation_position="top")
        fig8.update_layout(**chart_layout(
            height=300, margin=dict(l=8, r=30, t=8, b=8),
            xaxis=grid_axis("% of WHO 24h guideline"),
            yaxis=dict(showgrid=False),
        ))
        st.plotly_chart(fig8, width="stretch")
        legend_row([("≤100% Good", COLORS["good"]), ("100–200% Moderate", COLORS["warning"]),
                    ("200–300% Poor", COLORS["serious"]), (">300% Severe", COLORS["critical"])])
        st.caption("Reference levels are illustrative (WHO 2021 guideline), not a live regulatory index.")

    with c2:
        section_label(f"US AQI trend (next {chart_days} days)")
        aq_window = aq_df[aq_df["time"] < window_end]
        fig9 = go.Figure()
        aqi_bands = [(0, 50, COLORS["good"]), (50, 100, COLORS["warning"]),
                     (100, 150, COLORS["serious"]), (150, 300, COLORS["critical"])]
        for y0, y1, color in aqi_bands:
            fig9.add_hrect(y0=y0, y1=y1, fillcolor=color, opacity=0.08, line_width=0, layer="below")
        fig9.add_trace(go.Scatter(
            x=aq_window["time"], y=aq_window["us_aqi"], mode="lines",
            line=dict(color=COLORS["blue"], width=2.5), showlegend=False,
            hovertemplate="%{x|%a %H:%M}<br>AQI %{y:.0f}<extra></extra>",
        ))
        fig9.update_layout(**chart_layout(
            height=300,
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=False, title="US AQI"),
        ))
        st.plotly_chart(fig9, width="stretch")
        legend_row([("Good", COLORS["good"]), ("Moderate", COLORS["warning"]),
                    ("Unhealthy (sensitive)", COLORS["serious"]), ("Unhealthy+", COLORS["critical"])])

# --- History ---------------------------------------------------------------
with tab_history:
    section_label(f"Temperature: last {history_days} days vs. next {forecast_days} days")
    daily_df["mean_temp"] = (daily_df["temperature_2m_max"] + daily_df["temperature_2m_min"]) / 2
    past = daily_df[daily_df["date"] <= today_date]
    future = daily_df[daily_df["date"] >= today_date]

    fig10 = go.Figure()
    fig10.add_trace(go.Scatter(
        x=daily_df["date"], y=daily_df["temperature_2m_max"],
        line=dict(width=0), showlegend=False, hoverinfo="skip",
    ))
    fig10.add_trace(go.Scatter(
        x=daily_df["date"], y=daily_df["temperature_2m_min"],
        line=dict(width=0), fill="tonexty", fillcolor=f"rgba({COLORS['blue_rgb']},0.08)",
        showlegend=False, hoverinfo="skip", name="Daily range",
    ))
    fig10.add_trace(go.Scatter(
        x=past["date"], y=past["mean_temp"], mode="lines", name="Past (actual)",
        line=dict(color=COLORS["muted"], width=2),
        hovertemplate="%{x|%a %b %d}<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig10.add_trace(go.Scatter(
        x=future["date"], y=future["mean_temp"], mode="lines", name="Forecast",
        line=dict(color=COLORS["blue"], width=2.5),
        hovertemplate="%{x|%a %b %d}<br>%{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig10.add_vline(x=pd.Timestamp(today_date), line_dash="dot", line_color=COLORS["text_secondary"],
                     annotation_text="Today", annotation_position="top")
    fig10.update_layout(**chart_layout(
        height=360,
        legend=TOP_LEGEND,
        xaxis=dict(showgrid=False),
        yaxis=grid_axis(temp_symbol),
        hovermode="x unified",
    ))
    st.plotly_chart(fig10, width="stretch")

    section_label("Daylight duration across the forecast")
    fig11 = go.Figure(go.Scatter(
        x=forecast_daily_df["date"], y=forecast_daily_df["daylight_duration"] / 3600,
        mode="lines+markers", line=dict(color=COLORS["blue"], width=2.5, shape="spline"),
        fill="tozeroy", fillcolor=f"rgba({COLORS['blue_rgb']},0.08)",
        hovertemplate="%{x|%a %b %d}<br>%{y:.1f} hrs daylight<extra></extra>",
    ))
    fig11.update_layout(**chart_layout(
        height=280, showlegend=False,
        xaxis=dict(showgrid=False),
        yaxis=grid_axis("Hours"),
    ))
    st.plotly_chart(fig11, width="stretch")

st.divider()
with st.expander("View forecast as a table"):
    table_rows = [
        {
            "Date": d["date"].isoformat(),
            f"High ({temp_symbol})": round(d["temperature_2m_max"], 1),
            f"Low ({temp_symbol})": round(d["temperature_2m_min"], 1),
            "Condition": WMO_TEXT.get(int(d["weather_code"]), ""),
            "Rain chance (%)": d["precipitation_probability_max"],
            f"Precipitation ({precip_unit})": round(d["precipitation_sum"], 1),
            "UV max": d["uv_index_max"],
        }
        for _, d in forecast_daily_df.iterrows()
    ]
    st.dataframe(pd.DataFrame(table_rows), width="stretch", hide_index=True)
