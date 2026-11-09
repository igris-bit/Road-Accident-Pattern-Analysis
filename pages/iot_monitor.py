"""
pages/iot_monitor.py
--------------------
IoT Simulation & Alert Monitoring — New Streamlit Page.

This file  lives in the `pages/` folder so Streamlit automatically adds it
to the sidebar navigation without touching app.py.

Features:
  1. Live Sensor Feed       — Real-time simulated IoT readings with auto-refresh
  2. Smart Alert Panel      — Colour-coded alerts based on accident risk
  3. Risk Gauge             — Visual risk percentage with status indicator
  4. Accident Hotspot Map   — Interactive map of real accident locations
  5. Alert History Log      — Session-based alert records with CSV download
  6. Risk Prediction        — Multi-factor accident risk assessment
  7. City Statistics        — Historical accident data by city
  8. Emergency Warnings     — Automatic alerts for high-risk situations
"""


import time
import datetime
import pandas as pd
import numpy as np
import streamlit as st

# Import our simulation engine (one level up)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from iot_simulator import (
    generate_sensor_reading,
    evaluate_alert,
    get_city_historical_stats,
    CITIES,
)

# ─────────────────────────────────────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="IoT Monitor — Road Accident Analysis",
    page_icon="📡",
    layout="wide",
)

# ─────────────────────────────────────────────────────────────────────────────
# Custom CSS
# ─────────────────────────────────────────────────────────────────────────────

st.markdown("""
<style>
    .alert-box {
        padding: 14px 18px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-size: 15px;
        font-weight: 500;
    }
    .sensor-card {
        background: #f0f2f6;
        border-radius: 10px;
        padding: 14px;
        margin-bottom: 8px;
    }
    .gauge-label {
        font-size: 13px;
        color: #555;
        margin-bottom: 2px;
    }
    .section-title {
        font-size: 20px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 6px;
    }
    .history-header {
        font-size: 12px;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Session state — initialise alert log
# ─────────────────────────────────────────────────────────────────────────────

if "alert_log" not in st.session_state:
    st.session_state.alert_log = []   # list of dicts

if "last_reading" not in st.session_state:
    st.session_state.last_reading = None

if "last_alert" not in st.session_state:
    st.session_state.last_alert = None

# ─────────────────────────────────────────────────────────────────────────────
# Load real dataset (cached)
# ─────────────────────────────────────────────────────────────────────────────

@st.cache_data
def load_real_dataset():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base, "indian_roads_dataset.csv")
    df = pd.read_csv(csv_path)
    if "festival" in df.columns:
        df = df.drop(columns=["festival"])
    df = df.drop_duplicates().dropna()
    return df

try:
    real_df = load_real_dataset()
    dataset_loaded = True
except Exception as e:
    st.warning(f"Could not load dataset for map/stats: {e}")
    real_df = pd.DataFrame()
    dataset_loaded = False

# ─────────────────────────────────────────────────────────────────────────────
# Sidebar — Simulation Controls
# ─────────────────────────────────────────────────────────────────────────────

st.sidebar.title("📡 IoT Simulation Controls")
st.sidebar.markdown("---")

selected_city = st.sidebar.selectbox(
    "📍 Select City for Sensor",
    options=["🎲 Random"] + sorted(CITIES),
)
city_arg = None if selected_city == "🎲 Random" else selected_city

auto_refresh = st.sidebar.toggle("⚡ Auto-Refresh (every 5 sec)", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗺️ Map Options")
show_map = st.sidebar.toggle("Show Accident Hotspot Map", value=True)
map_severity = st.sidebar.multiselect(
    "Severity to show",
    options=["minor", "major", "fatal"],
    default=["major", "fatal"],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**How it works**\n\n"
    "This module simulates roadside IoT sensors.\n"
    "Each reading contains the same fields as the real dataset.\n"
    "The alert engine applies rule-based checks to flag hazards."
)

# ─────────────────────────────────────────────────────────────────────────────
# Page Header
# ─────────────────────────────────────────────────────────────────────────────

st.title("📡 IoT Simulation & Alert Monitoring")
st.markdown(
    "Real-time simulation of roadside IoT sensors with automatic hazard detection. "
    "No physical hardware required — sensor readings are generated from the same "
    "data distribution as the **Indian Roads Dataset**."
)
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Section 1 — Generate / Auto-refresh reading
# ─────────────────────────────────────────────────────────────────────────────

col_btn, col_status = st.columns([1, 3])

with col_btn:
    manual_trigger = st.button("🔄 Generate New Reading", use_container_width=True)

if manual_trigger or auto_refresh:
    reading = generate_sensor_reading(city=city_arg)
    alert   = evaluate_alert(reading)

    st.session_state.last_reading = reading
    st.session_state.last_alert   = alert

    # Append to alert log (skip SAFE entries optionally)
    log_entry = {
        "Timestamp":       reading["timestamp"],
        "City":            reading["city"],
        "Weather":         reading["weather"],
        "Visibility":      reading["visibility"],
        "Temp (°C)":       reading["temperature"],
        "Traffic":         reading["traffic_density"],
        "Speed (km/h)":    reading.get("vehicle_speed", "N/A"),
        "Road Surface":    reading.get("road_condition", "N/A"),
        "Risk Score":      reading["risk_score"],
        "Alert Level":     alert["level"],
        "Alert Message":   " | ".join(alert["messages"]),
    }
    st.session_state.alert_log.insert(0, log_entry)
    # Keep last 100 entries only
    st.session_state.alert_log = st.session_state.alert_log[:100]

# ─────────────────────────────────────────────────────────────────────────────
# Section 2 — Live Sensor Reading Display
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">🌡️ Live Sensor Reading</div>', unsafe_allow_html=True)

if st.session_state.last_reading is None:
    st.info("👆 Click **Generate New Reading** to start the simulation.")
else:
    r = st.session_state.last_reading
    a = st.session_state.last_alert

    # ── Sensor fields in metric cards ──
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("📍 City",          r["city"])
    c2.metric("🌤️ Weather",       r["weather"].capitalize())
    c3.metric("👁️ Visibility",    r["visibility"].capitalize())
    c4.metric("🌡️ Temp",          f"{r['temperature']} °C")
    c5.metric("🚗 Traffic",       r["traffic_density"].capitalize())
    c6.metric("🕐 Hour",          f"{r['hour']:02d}:00")

    c7, c8, c9, c10, c11, c12 = st.columns(6)
    c7.metric("🛣️ Road Type",     r["road_type"].capitalize())
    c8.metric("⚠️ Peak Hour",     "Yes" if r["is_peak_hour"] else "No")
    c9.metric("🏎️ Avg Speed",     f"{r.get('vehicle_speed', 'N/A')} km/h")
    c10.metric("🛤️ Surface",      r.get("road_condition", "N/A").capitalize())
    c11.metric("📶 Sensor",        r.get("sensor_status", "N/A").capitalize())
    c12.metric("🗓️ Day",          r["day_of_week"])

    st.caption(f"⏱️ Reading timestamp: **{r['timestamp']}**  |  📌 Lat: {r['latitude']}, Lon: {r['longitude']}")

    st.markdown("---")

    # ── Section 3: Alert Panel ──
    st.markdown('<div class="section-title">🚨 Alert Panel</div>', unsafe_allow_html=True)

    alert_bg = {"HIGH": "#ffe0e0", "MEDIUM": "#fff3cd", "LOW": "#e0ecff", "SAFE": "#d4edda"}
    alert_border = {"HIGH": "#FF4B4B", "MEDIUM": "#FFA500", "LOW": "#4B9EFF", "SAFE": "#21BA45"}

    level = a["level"]
    bg    = alert_bg[level]
    bdr   = alert_border[level]

    st.markdown(
        f'<div class="alert-box" style="background:{bg}; border-left: 5px solid {bdr};">'
        f'<b>{a["emoji"]} Alert Level: {level}</b><br/>'
        + "<br/>".join(a["messages"])
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # ── Section 4: Risk Gauge ──
    st.markdown('<div class="section-title">📊 Risk Score Gauge</div>', unsafe_allow_html=True)

    risk = r["risk_score"]
    gauge_col1, gauge_col2 = st.columns([3, 1])

    with gauge_col1:
        # Progress bar colored by risk
        st.markdown('<p class="gauge-label">Risk Score (0.0 = Safe → 1.0 = Extreme)</p>', unsafe_allow_html=True)
        st.progress(risk)

        # Colour legend
        leg1, leg2, leg3, leg4 = st.columns(4)
        leg1.markdown("🟢 **0.0–0.24** Safe")
        leg2.markdown("🔵 **0.25–0.44** Low")
        leg3.markdown("🟡 **0.45–0.69** Medium")
        leg4.markdown("🔴 **0.70–1.0** High")

    with gauge_col2:
        gauge_emoji = "🟢" if risk < 0.25 else ("🔵" if risk < 0.45 else ("🟡" if risk < 0.70 else "🔴"))
        st.markdown(
            f"<div style='text-align:center; font-size:60px; margin-top:10px'>{gauge_emoji}</div>"
            f"<div style='text-align:center; font-size:28px; font-weight:bold'>{risk:.2f}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Section 5: Historical Context for this City ──
    if dataset_loaded:
        st.markdown('<div class="section-title">📋 Historical Context — Real Dataset</div>', unsafe_allow_html=True)
        stats = get_city_historical_stats(real_df, r["city"])

        if stats["found"]:
            sc1, sc2, sc3, sc4, sc5 = st.columns(5)
            sc1.metric("Total Accidents", f"{stats['total']:,}", help="In real dataset")
            sc2.metric("Fatal Accidents", f"{stats['fatal']:,}", f"{stats['fatal_pct']}%")
            sc3.metric("Avg Risk Score", f"{stats['avg_risk']:.3f}")
            sc4.metric("Top Cause", stats["top_cause"].capitalize())
            sc5.metric("Peak Accident Hour", f"{stats['peak_hour']:02d}:00")
        else:
            st.info(f"No historical records found for **{r['city']}** in the dataset.")

        st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Section 6 — Accident Hotspot Map
# ─────────────────────────────────────────────────────────────────────────────

if show_map and dataset_loaded:
    st.markdown('<div class="section-title">🗺️ Accident Hotspot Map (Real Dataset)</div>', unsafe_allow_html=True)

    try:
        import pydeck as pdk

        map_df = real_df[real_df["accident_severity"].isin(map_severity)][
            ["latitude", "longitude", "accident_severity", "city", "risk_score"]
        ].dropna()

        # Limit to 5000 points for performance
        if len(map_df) > 5000:
            map_df = map_df.sample(5000, random_state=42)

        # Colour by severity
        severity_color = {
            "minor": [70, 130, 180, 140],    # steel-blue
            "major": [255, 165, 0, 180],      # orange
            "fatal": [220, 20, 60, 220],      # crimson
        }
        map_df["color"] = map_df["accident_severity"].map(severity_color)

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=map_df,
            get_position="[longitude, latitude]",
            get_color="color",
            get_radius=800,
            pickable=True,
        )

        # If we have a simulated sensor reading, mark it
        extra_layers = [layer]
        if st.session_state.last_reading:
            sensor_pt = pd.DataFrame([{
                "latitude":  st.session_state.last_reading["latitude"],
                "longitude": st.session_state.last_reading["longitude"],
            }])
            sensor_layer = pdk.Layer(
                "ScatterplotLayer",
                data=sensor_pt,
                get_position="[longitude, latitude]",
                get_color=[0, 255, 0, 255],
                get_radius=2500,
                pickable=False,
            )
            extra_layers.append(sensor_layer)

        view = pdk.ViewState(
            latitude=20.5937,
            longitude=78.9629,
            zoom=4.5,
            pitch=0,
        )

        st.pydeck_chart(pdk.Deck(
            layers=extra_layers,
            initial_view_state=view,
            tooltip={"text": "City: {city}\nSeverity: {accident_severity}\nRisk: {risk_score}"},
            map_style="mapbox://styles/mapbox/dark-v9",
        ))

        col_leg1, col_leg2, col_leg3, col_leg4 = st.columns(4)
        col_leg1.markdown("🔵 Minor accidents")
        col_leg2.markdown("🟠 Major accidents")
        col_leg3.markdown("🔴 Fatal accidents")
        col_leg4.markdown("🟢 Current IoT sensor location")

    except ImportError:
        st.warning("pydeck not installed. Run: `pip install pydeck`")
        st.info("Showing tabular location data instead:")
        st.dataframe(
            real_df[real_df["accident_severity"].isin(map_severity)][
                ["city", "state", "latitude", "longitude", "accident_severity", "risk_score"]
            ].head(50),
            use_container_width=True,
        )

    st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Section 7 — Alert History Log
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">📜 Alert History Log</div>', unsafe_allow_html=True)

if not st.session_state.alert_log:
    st.info("No alerts generated yet. Click **Generate New Reading** to start.")
else:
    log_df = pd.DataFrame(st.session_state.alert_log)

    # Summary counters
    count_high   = (log_df["Alert Level"] == "HIGH").sum()
    count_medium = (log_df["Alert Level"] == "MEDIUM").sum()
    count_low    = (log_df["Alert Level"] == "LOW").sum()
    count_safe   = (log_df["Alert Level"] == "SAFE").sum()

    lc1, lc2, lc3, lc4, lc5 = st.columns(5)
    lc1.metric("Total Readings", len(log_df))
    lc2.metric("🔴 HIGH",   count_high)
    lc3.metric("🟡 MEDIUM", count_medium)
    lc4.metric("🔵 LOW",    count_low)
    lc5.metric("🟢 SAFE",   count_safe)

    # Colour rows by alert level
    def _row_color(row):
        colors = {
            "HIGH":   "background-color: #ffe0e0",
            "MEDIUM": "background-color: #fff3cd",
            "LOW":    "background-color: #e0ecff",
            "SAFE":   "background-color: #d4edda",
        }
        return [colors.get(row["Alert Level"], "")] * len(row)

    styled_log = log_df.style.apply(_row_color, axis=1)
    st.dataframe(styled_log, use_container_width=True, hide_index=True)

    # Download button
    csv_bytes = log_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Alert Log as CSV",
        data=csv_bytes,
        file_name=f"iot_alert_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
    )

    if st.button("🗑️ Clear Alert Log"):
        st.session_state.alert_log = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# Auto-refresh loop (must be LAST)
# ─────────────────────────────────────────────────────────────────────────────

if auto_refresh:
    time.sleep(5)
    st.rerun()
