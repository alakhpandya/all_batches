 # Weather Dashboard

A Streamlit dashboard for current conditions, a multi-day forecast, air quality,
and historical trends, powered entirely by [Open-Meteo](https://open-meteo.com/)
— a free weather API that needs **no API key**.

## Features

- Current conditions: temperature, feels-like, humidity, wind, pressure, UV, air quality
- City search with geocoding (handles ambiguous names, e.g. "Springfield")
- 3–14 day forecast cards with condition icons and rain chance
- **Overview**: today's hourly temperature vs. feels-like
- **Temperature**: daily high/low, daily precipitation, hour-by-hour heatmap across the forecast
- **Wind & UV**: wind speed/gusts trend, wind rose (direction × speed frequency), UV index with risk bands
- **Air Quality**: pollutant breakdown (PM2.5, PM10, NO₂, O₃, SO₂, CO) vs. WHO guideline levels, US AQI trend
- **History**: temperature trend across the past N days and next N days (with daily range band), daylight duration trend
- Celsius/Fahrenheit + km/h/mph toggle, adjustable forecast horizon and history window
- Recent-search history in the sidebar
- Forecast table view
- Apple-inspired design with a working light/dark mode toggle (sidebar)

## Setup

> **Always use a virtual environment (venv).** Create it once, and activate it
> every time before installing packages or running the app.

1. Create the virtual environment (one time):

   ```
   python -m venv .venv
   ```

2. Activate it (every new terminal session):

   - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
   - Windows (cmd): `.venv\Scripts\activate.bat`
   - macOS / Linux: `source .venv/bin/activate`

3. Install dependencies (inside the activated venv):

   ```
   pip install -r requirements.txt
   ```

4. Run the app — no API key or configuration needed:

   ```
   python -m streamlit run app.py
   ```

   Running via `python -m streamlit` guarantees the app uses the venv's
   Python and packages.

## Data sources

All calls go to Open-Meteo's free, keyless endpoints:

- Geocoding API — resolves a city name to coordinates
- Forecast API — current conditions, hourly and daily forecast (up to 16 days), plus
  up to 92 days of history via `past_days`
- Air Quality API — hourly PM2.5, PM10, NO₂, O₃, SO₂, CO and US AQI

Forecast and air-quality responses are cached for 10 minutes; geocoding results
are cached for 24 hours.
