import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(page_title="Weather App", page_icon="⛅", layout="wide")

GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
AIR_QUALITY_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"

# ---- Palette (validated categorical / status colors) ----
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
GOOD, WARNING, SERIOUS, CRITICAL = "#0ca30c", "#fab219", "#ec835a", "#d03b3b"

POPULAR_CITIES = ["New York", "London", "Tokyo", "Mumbai", "Paris", "Sydney", "Dubai", "Singapore"]

# WMO weather interpretation codes -> (icon, description)
WEATHER_CODES = {
    0: ("☀️", "Clear Sky"), 1: ("🌤️", "Mainly Clear"), 2: ("⛅", "Partly Cloudy"),
    3: ("☁️", "Overcast"), 45: ("🌫️", "Fog"), 48: ("🌫️", "Depositing Rime Fog"),
    51: ("🌦️", "Light Drizzle"), 53: ("🌦️", "Moderate Drizzle"), 55: ("🌦️", "Dense Drizzle"),
    56: ("🌧️", "Light Freezing Drizzle"), 57: ("🌧️", "Dense Freezing Drizzle"),
    61: ("🌧️", "Slight Rain"), 63: ("🌧️", "Moderate Rain"), 65: ("🌧️", "Heavy Rain"),
    66: ("🌧️", "Light Freezing Rain"), 67: ("🌧️", "Heavy Freezing Rain"),
    71: ("❄️", "Slight Snow"), 73: ("❄️", "Moderate Snow"), 75: ("❄️", "Heavy Snow"),
    77: ("❄️", "Snow Grains"), 80: ("🌦️", "Slight Rain Showers"), 81: ("🌦️", "Moderate Rain Showers"),
    82: ("🌧️", "Violent Rain Showers"), 85: ("🌨️", "Slight Snow Showers"), 86: ("🌨️", "Heavy Snow Showers"),
    95: ("⛈️", "Thunderstorm"), 96: ("⛈️", "Thunderstorm with Slight Hail"), 99: ("⛈️", "Thunderstorm with Heavy Hail"),
}


def describe(code: int):
    return WEATHER_CODES.get(code, ("🌡️", "Unknown"))


def aqi_category(aqi: int):
    if aqi is None:
        return "Unknown", "#898781"
    if aqi <= 50:
        return "Good", GOOD
    if aqi <= 100:
        return "Moderate", WARNING
    if aqi <= 150:
        return "Unhealthy (Sensitive)", SERIOUS
    if aqi <= 200:
        return "Unhealthy", SERIOUS
    if aqi <= 300:
        return "Very Unhealthy", CRITICAL
    return "Hazardous", CRITICAL


@st.cache_data(ttl=3600, show_spinner=False)
def geocode_city(city: str):
    response = requests.get(GEOCODE_URL, params={"name": city, "count": 5}, timeout=10)
    response.raise_for_status()
    return response.json().get("results") or []


@st.cache_data(ttl=600, show_spinner=False)
def fetch_weather(lat: float, lon: float, temp_unit: str, wind_unit: str, forecast_days: int):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,apparent_temperature,relative_humidity_2m,weather_code,"
                    "wind_speed_10m,wind_direction_10m,surface_pressure,is_day",
        "hourly": "temperature_2m,precipitation_probability,wind_speed_10m,visibility,weather_code",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,"
                 "uv_index_max,sunrise,sunset,wind_speed_10m_max",
        "temperature_unit": temp_unit,
        "wind_speed_unit": wind_unit,
        "timezone": "auto",
        "forecast_days": forecast_days,
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


@st.cache_data(ttl=1800, show_spinner=False)
def fetch_air_quality(lat: float, lon: float):
    params = {"latitude": lat, "longitude": lon, "current": "us_aqi,pm2_5,pm10,european_aqi", "timezone": "auto"}
    response = requests.get(AIR_QUALITY_URL, params=params, timeout=10)
    if response.status_code != 200:
        return None
    return response.json().get("current")


# ---------------------------------------------------------------- styling
st.markdown("""
<style>
:root{
  --surface-1:#fcfcfb; --text-secondary:#52514e; --muted:#898781;
  --border: rgba(11,11,11,0.10); --blue:#2a78d6; --blue-dark:#184f95;
}
@media (prefers-color-scheme: dark){
  :root{
    --surface-1:#232323; --text-secondary:#c3c2b7; --muted:#898781;
    --border: rgba(255,255,255,0.12); --blue:#3987e5; --blue-dark:#184f95;
  }
}
.block-container{padding-top:2rem;}
.hero-card{
  background: linear-gradient(135deg, var(--blue), var(--blue-dark));
  color:#fff; border-radius:20px; padding:2rem 2.2rem;
  box-shadow: 0 10px 28px rgba(0,0,0,0.18); margin-bottom:1.2rem;
}
.hero-top{display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:1rem;}
.hero-loc{font-size:1.4rem; font-weight:600;}
.hero-time{opacity:0.85; font-size:0.9rem;}
.hero-temp{font-size:4.2rem; font-weight:700; line-height:1;}
.hero-desc{font-size:1.15rem; opacity:0.92;}
.hero-icon{font-size:4.5rem; line-height:1;}
.hero-minmax{opacity:0.9; font-size:0.95rem; margin-top:0.3rem;}
.day-card{
  background:var(--surface-1); border:1px solid var(--border); border-radius:14px;
  padding:0.9rem 0.5rem; text-align:center;
}
.day-card .d{font-weight:600; font-size:0.95rem;}
.day-card .icon{font-size:1.8rem; margin:0.2rem 0;}
.day-card .hi{font-weight:700;}
.day-card .lo{color:var(--muted);}
.day-card .rain{font-size:0.8rem; color:var(--text-secondary); margin-top:0.2rem;}
.aqi-badge{
  display:inline-block; padding:0.4rem 1rem; border-radius:999px; color:#fff;
  font-weight:600; font-size:1rem;
}
[data-testid="stMetric"]{
  background:var(--surface-1); border:1px solid var(--border); border-radius:14px; padding:0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------- session state
if "city" not in st.session_state:
    st.session_state.city = "London"
if "recent" not in st.session_state:
    st.session_state.recent = []

# ---------------------------------------------------------------- sidebar
with st.sidebar:
    st.header("📍 Location")
    city_query = st.text_input("Search a city", value=st.session_state.city, key="city_text")

    st.caption("Popular cities")
    pop_cols = st.columns(2)
    for i, pc in enumerate(POPULAR_CITIES):
        if pop_cols[i % 2].button(pc, use_container_width=True, key=f"pop_{pc}"):
            st.session_state.city = pc
            st.rerun()

    if st.session_state.recent:
        st.caption("Recent searches")
        for rc in st.session_state.recent[:5]:
            if st.button(f"🕘 {rc}", use_container_width=True, key=f"recent_{rc}"):
                st.session_state.city = rc
                st.rerun()

    st.divider()
    st.header("⚙️ Settings")
    unit_choice = st.radio("Temperature unit", ["Celsius", "Fahrenheit"], horizontal=True)
    temp_unit = "celsius" if unit_choice == "Celsius" else "fahrenheit"
    wind_unit = "kmh" if unit_choice == "Celsius" else "mph"
    temp_symbol = "°C" if unit_choice == "Celsius" else "°F"

    forecast_days = st.slider("Forecast range (days)", min_value=3, max_value=16, value=7)
    hourly_window = st.select_slider("Hourly chart window", options=[12, 24, 48, 72], value=24)

    st.divider()
    show_air_quality = st.checkbox("Show air quality", value=True)
    show_map = st.checkbox("Show map", value=True)

    st.divider()
    if st.button("🔄 Refresh data", use_container_width=True):
        st.cache_data.clear()
        st.rerun()

    st.caption("Data: [Open-Meteo](https://open-meteo.com) — free, no API key required")

# ---------------------------------------------------------------- main
st.title("⛅ Weather App")

if city_query:
    st.session_state.city = city_query

if not st.session_state.city:
    st.info("Enter a city in the sidebar to get started.")
    st.stop()

with st.spinner("Looking up location..."):
    matches = geocode_city(st.session_state.city)

if not matches:
    st.error(f"City '{st.session_state.city}' not found. Check the spelling and try again.")
    st.stop()

if len(matches) > 1:
    labels = [f"{m['name']}, {m.get('admin1', '')} {m.get('country', '')}".strip() for m in matches]
    picked = st.selectbox("Multiple matches found — pick one", options=range(len(matches)), format_func=lambda i: labels[i])
    location = matches[picked]
else:
    location = matches[0]

if st.session_state.city not in st.session_state.recent:
    st.session_state.recent.insert(0, st.session_state.city)
    st.session_state.recent = st.session_state.recent[:5]

lat, lon = location["latitude"], location["longitude"]
location_label = location["name"]
if location.get("admin1"):
    location_label += f", {location['admin1']}"
if location.get("country"):
    location_label += f", {location['country']}"

with st.spinner("Fetching weather..."):
    data = fetch_weather(lat, lon, temp_unit, wind_unit, forecast_days)

current = data["current"]
icon, description = describe(current["weather_code"])
today = data["daily"]

# ---------------------------------------------------------------- hero card
st.markdown(f"""
<div class="hero-card">
  <div class="hero-top">
    <div>
      <div class="hero-loc">📍 {location_label}</div>
      <div class="hero-time">{datetime.fromisoformat(current['time']).strftime('%A, %d %b %Y · %H:%M')} local time</div>
    </div>
    <div style="text-align:right;">
      <div class="hero-icon">{icon}</div>
    </div>
  </div>
  <div style="display:flex; align-items:flex-end; gap:1rem; margin-top:0.5rem;">
    <div class="hero-temp">{current['temperature_2m']:.0f}{temp_symbol}</div>
    <div class="hero-desc">{description}</div>
  </div>
  <div class="hero-minmax">Feels like {current['apparent_temperature']:.0f}{temp_symbol} · High {today['temperature_2m_max'][0]:.0f}{temp_symbol} / Low {today['temperature_2m_min'][0]:.0f}{temp_symbol}</div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------- metrics
sunrise = datetime.fromisoformat(today["sunrise"][0]).strftime("%H:%M")
sunset = datetime.fromisoformat(today["sunset"][0]).strftime("%H:%M")

m1, m2, m3, m4, m5, m6 = st.columns(6)
m1.metric("Humidity", f"{current['relative_humidity_2m']}%")
m2.metric("Wind", f"{current['wind_speed_10m']:.0f} {wind_unit}")
m3.metric("Pressure", f"{current['surface_pressure']:.0f} hPa")
m4.metric("UV Index", f"{today['uv_index_max'][0]:.1f}")
m5.metric("Sunrise", sunrise)
m6.metric("Sunset", sunset)

st.markdown("")

tab_overview, tab_charts, tab_air_map = st.tabs(["📅 Daily Forecast", "📈 Charts", "🌫️ Air Quality & Map"])

# ---------------------------------------------------------------- daily forecast
with tab_overview:
    st.subheader(f"{forecast_days}-Day Forecast")
    cols = st.columns(len(today["time"]))
    for col, date, code, tmax, tmin, rain in zip(
        cols, today["time"], today["weather_code"],
        today["temperature_2m_max"], today["temperature_2m_min"], today["precipitation_probability_max"],
    ):
        with col:
            day_icon, day_desc = describe(code)
            day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%a %d")
            st.markdown(f"""
            <div class="day-card">
              <div class="d">{day_name}</div>
              <div class="icon">{day_icon}</div>
              <div class="hi">{tmax:.0f}°</div>
              <div class="lo">{tmin:.0f}°</div>
              <div class="rain">💧 {rain}%</div>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------------------- charts
with tab_charts:
    hourly = data["hourly"]
    df_hourly = pd.DataFrame({
        "time": pd.to_datetime(hourly["time"]),
        "temperature": hourly["temperature_2m"],
        "precipitation_probability": hourly["precipitation_probability"],
        "wind_speed": hourly["wind_speed_10m"],
    })
    now = pd.to_datetime(current["time"])
    df_hourly = df_hourly[df_hourly["time"] >= now.floor("h")].head(hourly_window)

    st.subheader(f"Temperature — next {hourly_window}h")
    fig_temp = go.Figure()
    fig_temp.add_trace(go.Scatter(
        x=df_hourly["time"], y=df_hourly["temperature"], mode="lines",
        line=dict(color=BLUE, width=2, shape="spline"), fill="tozeroy",
        fillcolor="rgba(42,120,214,0.12)", name="Temperature",
        hovertemplate="%{x|%a %H:%M}<br>%{y:.1f}" + temp_symbol + "<extra></extra>",
    ))
    fig_temp.update_layout(
        height=320, margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title=f"Temp ({temp_symbol})", gridcolor="#e1e0d9"),
        xaxis=dict(gridcolor="#e1e0d9"), showlegend=False,
    )
    st.plotly_chart(fig_temp, use_container_width=True)

    st.subheader(f"Precipitation Probability — next {hourly_window}h")
    fig_rain = go.Figure()
    fig_rain.add_trace(go.Bar(
        x=df_hourly["time"], y=df_hourly["precipitation_probability"],
        marker_color=AQUA, name="Precipitation",
        hovertemplate="%{x|%a %H:%M}<br>%{y}%<extra></extra>",
    ))
    fig_rain.update_layout(
        height=280, margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title="Chance (%)", range=[0, 100], gridcolor="#e1e0d9"),
        xaxis=dict(gridcolor="#e1e0d9"), showlegend=False,
    )
    st.plotly_chart(fig_rain, use_container_width=True)

    st.subheader(f"Wind Speed — next {hourly_window}h")
    fig_wind = go.Figure()
    fig_wind.add_trace(go.Scatter(
        x=df_hourly["time"], y=df_hourly["wind_speed"], mode="lines+markers",
        line=dict(color=ORANGE, width=2), marker=dict(size=6),
        hovertemplate="%{x|%a %H:%M}<br>%{y:.0f} " + wind_unit + "<extra></extra>",
    ))
    fig_wind.update_layout(
        height=280, margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title=f"Wind ({wind_unit})", gridcolor="#e1e0d9"),
        xaxis=dict(gridcolor="#e1e0d9"), showlegend=False,
    )
    st.plotly_chart(fig_wind, use_container_width=True)

    st.subheader(f"{forecast_days}-Day Temperature Trend")
    df_daily = pd.DataFrame({
        "date": pd.to_datetime(today["time"]),
        "high": today["temperature_2m_max"],
        "low": today["temperature_2m_min"],
    })
    fig_trend = go.Figure()
    fig_trend.add_trace(go.Scatter(
        x=df_daily["date"], y=df_daily["high"], mode="lines+markers", name="High",
        line=dict(color=ORANGE, width=2), marker=dict(size=8),
        hovertemplate="%{x|%a %d %b}<br>High: %{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig_trend.add_trace(go.Scatter(
        x=df_daily["date"], y=df_daily["low"], mode="lines+markers", name="Low",
        line=dict(color=BLUE, width=2), marker=dict(size=8),
        hovertemplate="%{x|%a %d %b}<br>Low: %{y:.0f}" + temp_symbol + "<extra></extra>",
    ))
    fig_trend.update_layout(
        height=320, margin=dict(l=10, r=10, t=10, b=10),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(title=f"Temp ({temp_symbol})", gridcolor="#e1e0d9"),
        xaxis=dict(gridcolor="#e1e0d9"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# ---------------------------------------------------------------- air quality & map
with tab_air_map:
    if show_air_quality:
        aqi_data = fetch_air_quality(lat, lon)
        if aqi_data:
            label, color = aqi_category(aqi_data.get("us_aqi"))
            st.subheader("Air Quality")
            c1, c2 = st.columns([1, 2])
            with c1:
                st.markdown(f"""
                <div>
                  <div style="font-size:2.5rem; font-weight:700;">{aqi_data.get('us_aqi', '—')}</div>
                  <div class="aqi-badge" style="background:{color};">{label}</div>
                </div>
                """, unsafe_allow_html=True)
            with c2:
                a1, a2 = st.columns(2)
                a1.metric("PM2.5", f"{aqi_data.get('pm2_5', '—')} µg/m³")
                a2.metric("PM10", f"{aqi_data.get('pm10', '—')} µg/m³")
        else:
            st.info("Air quality data is not available for this location.")
        st.divider()

    if show_map:
        st.subheader("Location")
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}), zoom=9, size=200)
