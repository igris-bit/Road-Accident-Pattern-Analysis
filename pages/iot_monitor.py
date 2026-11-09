"""
pages/iot_monitor.py
--------------------
IoT Simulation & Alert Monitoring — Intelligent Transportation Systems (ITS).

Features:
  1. Live Sensor Feed          — Real-time simulated roadside IoT telemetry
  2. Smart Alert Engine        — Rule-based hazard evaluation
  3. Dynamic Highway VMS       — Overhead electronic LED signboard actuator
  4. Emergency CAD Dispatch    — Automated trauma hospital & highway patrol dispatch
  5. Risk Gauge                — Visual risk percentage with status indicator
  6. Historical Context Panel  — Real dataset metrics for the simulated city
  7. Accident Hotspot Map      — Interactive geospatial map of real accidents
  8. Alert History Log         — Session-based audit trail with CSV download
"""

import time
import datetime
import pandas as pd
import numpy as np
import streamlit as st
import sys
import os

# Import simulation engine (one level up)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from iot_simulator import (
    generate_sensor_reading,
    evaluate_alert,
    get_vms_actuator_display,
    get_emergency_dispatch_status,
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
        margin-top: 14px;
        margin-bottom: 8px;
    }
    .vms-sign-container {
        background: #090a0f;
        border: 4px solid #2a2e3d;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 10px;
        margin-bottom: 12px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.6);
        font-family: 'Consolas', 'Courier New', monospace;
    }
    .vms-header {
        font-size: 13px;
        letter-spacing: 3px;
        color: #8892b0;
        margin-bottom: 8px;
        text-transform: uppercase;
    }
    .vms-line {
        font-size: 21px;
        font-weight: 800;
        letter-spacing: 2px;
        line-height: 1.5;
        text-shadow: 0 0 10px currentColor;
    }
    .dispatch-box {
        background: #fdfdfd;
        border: 1px solid #e0e0e0;
        border-left: 6px solid #d9534f;
        border-radius: 8px;
        padding: 16px;
        margin-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# Session state
# ─────────────────────────────────────────────────────────────────────────────

if "alert_log" not in st.session_state:
    st.session_state.alert_log = []

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

st.sidebar.title("📡 IIoT Edge Controls")
st.sidebar.markdown("---")

selected_city = st.sidebar.selectbox(
    "📍 Select City Corridor",
    options=["🎲 Random Corridor"] + sorted(CITIES),
)
city_arg = None if selected_city == "🎲 Random Corridor" else selected_city

auto_refresh = st.sidebar.toggle("⚡ Live Telemetry Stream (every 5s)", value=False)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗺️ Hotspot Map Filters")
show_map = st.sidebar.toggle("Show Historical Hotspot Map", value=True)
map_severity = st.sidebar.multiselect(
    "Severity levels",
    options=["minor", "major", "fatal"],
    default=["major", "fatal"],
)

st.sidebar.markdown("---")
st.sidebar.info(
    "**IIoT Architecture**\n\n"
    "• **Perception Layer:** Roadside optical, weather, and traffic sensors.\n"
    "• **Network Layer:** Telemetry packet transmission (MQTT simulation).\n"
    "• **Application Layer:** Rule-based analytics, VMS actuation, and emergency CAD dispatch."
)

# ─────────────────────────────────────────────────────────────────────────────
# Page Header
# ─────────────────────────────────────────────────────────────────────────────

st.title("📡 IIoT Roadside Monitoring & Smart Actuation")
st.markdown(
    "Real-time simulation of roadside Industrial IoT sensors with automated hazard detection, "
    "dynamic highway Variable Message Sign (VMS) overrides, and emergency dispatch CAD interconnect."
)
st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Section 1 — Generate Reading
# ─────────────────────────────────────────────────────────────────────────────

col_btn, col_status = st.columns([1, 3])
with col_btn:
    manual_trigger = st.button("🔄 Pull Next Sensor Packet", use_container_width=True)

if manual_trigger or auto_refresh:
    reading = generate_sensor_reading(city=city_arg)
    alert   = evaluate_alert(reading)

    st.session_state.last_reading = reading
    st.session_state.last_alert   = alert

    log_entry = {
        "Timestamp":       reading["timestamp"],
        "City":            reading["city"],
        "Road Type":       reading["road_type"],
        "Weather":         reading["weather"],
        "Visibility":      reading["visibility"],
        "Avg Speed (km/h)": reading["avg_speed"],
        "Traffic":         reading["traffic_density"],
        "Risk Score":      reading["risk_score"],
        "Alert Level":     alert["level"],
        "Alert Message":   " | ".join(alert["messages"]),
    }
    st.session_state.alert_log.insert(0, log_entry)
    st.session_state.alert_log = st.session_state.alert_log[:100]

# ─────────────────────────────────────────────────────────────────────────────
# Section 2 — Live Sensor Reading Display
# ─────────────────────────────────────────────────────────────────────────────

st.markdown('<div class="section-title">🌡️ Roadside Sensor Telemetry</div>', unsafe_allow_html=True)

if st.session_state.last_reading is None:
    st.info("👆 Click **Pull Next Sensor Packet** to start the telemetry stream.")
else:
    r = st.session_state.last_reading
    a = st.session_state.last_alert

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("📍 City Corridor", r["city"])
    c2.metric("🌤️ Weather",       r["weather"].capitalize())
    c3.metric("👁️ Visibility",    r["visibility"].capitalize())
    c4.metric("🌡️ Ambient Temp",  f"{r['temperature']} °C")
    c5.metric("🚗 Traffic Density", r["traffic_density"].capitalize())
    c6.metric("⏱️ Avg Corridor Speed", f"{r['avg_speed']} km/h")

    c7, c8, c9, c10, c11 = st.columns(5)
    c7.metric("🛣️ Road Type",     r["road_type"].capitalize())
    c8.metric("⚠️ Peak Hour",     "Yes" if r["is_peak_hour"] else "No")
    c9.metric("📅 Weekend",       "Yes" if r["is_weekend"] else "No")
    c10.metric("🛣️ Lanes",        r["lanes"])
    c11.metric("🚦 Signal Present", "Yes" if r["traffic_signal"] else "No")

    st.caption(f"⏱️ Telemetry Timestamp: **{r['timestamp']}** | 📌 Sensor Node Lat: {r['latitude']}, Lon: {r['longitude']}")

    st.markdown("---")

    # ── Section 3: Alert & Actuation ──
    col_alert, col_vms = st.columns([1, 1])

    with col_alert:
        st.markdown('<div class="section-title">🚨 Hazard Alert Engine</div>', unsafe_allow_html=True)
        alert_bg = {"HIGH": "#ffe0e0", "MEDIUM": "#fff3cd", "LOW": "#e0ecff", "SAFE": "#d4edda"}
        alert_border = {"HIGH": "#FF4B4B", "MEDIUM": "#FFA500", "LOW": "#4B9EFF", "SAFE": "#21BA45"}

        level = a["level"]
        bg    = alert_bg[level]
        bdr   = alert_border[level]

        st.markdown(
            f'<div class="alert-box" style="background:{bg}; border-left: 5px solid {bdr};">'
            f'<b>{a["emoji"]} Priority Level: {level}</b><br/>'
            + "<br/>".join(a["messages"])
            + "</div>",
            unsafe_allow_html=True,
        )

        st.markdown('<p class="gauge-label">Calculated Corridor Risk Index</p>', unsafe_allow_html=True)
        st.progress(r["risk_score"])
        leg1, leg2, leg3, leg4 = st.columns(4)
        leg1.caption("🟢 Safe (<0.45)")
        leg2.caption("🔵 Low (0.45)")
        leg3.caption("🟡 Med (0.45-0.7)")
        leg4.caption("🔴 High (>0.7)")

    with col_vms:
        st.markdown('<div class="section-title">💡 Smart VMS Highway Actuator</div>', unsafe_allow_html=True)
        vms = get_vms_actuator_display(r, a)
        st.markdown(
            f"""
            <div class="vms-sign-container" style="background:{vms['sign_bg']};">
                <div class="vms-header">═══ SMART HIGHWAY VARIABLE MESSAGE SIGN ═══</div>
                <div class="vms-line" style="color: {vms['led_color']};">{vms['sign_title']}</div>
                <div class="vms-line" style="color: {vms['led_color']}; font-size:17px; margin-top:4px;">{vms['line_1']}</div>
                <div class="vms-line" style="color: #FFFFFF; font-size:18px; margin-top:4px;">{vms['line_2']}</div>
                <div class="vms-line" style="color: {vms['led_color']}; font-size:15px; margin-top:4px;">{vms['line_3']}</div>
                <div class="vms-header" style="margin-top:10px;">STATUS: {vms['status_text']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ── Section 4: Emergency CAD Dispatch Interconnect ──
    st.markdown('<div class="section-title">🚑 Automated Emergency Services CAD Dispatch</div>', unsafe_allow_html=True)
    cad = get_emergency_dispatch_status(r, a)

    cad_col1, cad_col2, cad_col3, cad_col4 = st.columns(4)
    with cad_col1:
        st.metric("CAD Response Status", cad["status"], delta="ACTIVE" if cad["activated"] else "NORMAL", delta_color="inverse" if cad["activated"] else "normal")
    with cad_col2:
        st.metric("Nearest Trauma Hospital", cad["hospital"])
        st.caption(f"Estimated Distance: **{cad['hospital_dist']}**")
    with cad_col3:
        st.metric("Highway Patrol Interceptor", cad["police_unit"])
        st.caption(f"Assigned Patrol ID: **{cad['police_id']}**")
    with cad_col4:
        st.metric("Ambulance Unit ETA", cad["eta"])
        st.caption(f"Dispatched Vehicle: **{cad['ambulance_id']}**")

    st.markdown("---")

    # ── Section 5: Historical Context for this City ──
    if dataset_loaded:
        st.markdown('<div class="section-title">📋 Corridor Historical Profile (Indian Roads Dataset)</div>', unsafe_allow_html=True)
        stats = get_city_historical_stats(real_df, r["city"])

        if stats["found"]:
            sc1, sc2, sc3, sc4, sc5 = st.columns(5)
            sc1.metric("Historical Accidents", f"{stats['total']:,}")
            sc2.metric("Fatal Accidents", f"{stats['fatal']:,}", f"{stats['fatal_pct']}% of total")
            sc3.metric("Historical Avg Risk", f"{stats['avg_risk']:.3f}")
            sc4.metric("Leading Accident Cause", stats["top_cause"].capitalize())
            sc5.metric("Peak Incident Hour", f"{stats['peak_hour']:02d}:00")
        else:
            st.info(f"No historical records found for **{r['city']}** in the dataset.")

        st.markdown("---")

# ─────────────────────────────────────────────────────────────────────────────
# Section 6 — Accident Hotspot Map
# ─────────────────────────────────────────────────────────────────────────────

if show_map and dataset_loaded:
    st.markdown('<div class="section-title">🗺️ Accident Hotspot Map & Live Sensor Position</div>', unsafe_allow_html=True)

    try:
        import pydeck as pdk

        map_df = real_df[real_df["accident_severity"].isin(map_severity)][
            ["latitude", "longitude", "accident_severity", "city", "risk_score"]
        ].dropna()

        if len(map_df) > 5000:
            map_df = map_df.sample(5000, random_state=42)

        severity_color = {
            "minor": [70, 130, 180, 140],
            "major": [255, 165, 0, 180],
            "fatal": [220, 20, 60, 220],
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
                get_color=[0, 255, 100, 255],
                get_radius=3000,
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
        col_leg4.markdown("🟢 Live IoT Sensor Node")

    except ImportError:
        st.warning("pydeck not installed.")
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

st.markdown('<div class="section-title">📜 IoT Incident & Alert Audit Log</div>', unsafe_allow_html=True)

if not st.session_state.alert_log:
    st.info("No telemetry packets processed yet. Click **Pull Next Sensor Packet** to begin logging.")
else:
    log_df = pd.DataFrame(st.session_state.alert_log)

    count_high   = (log_df["Alert Level"] == "HIGH").sum()
    count_medium = (log_df["Alert Level"] == "MEDIUM").sum()
    count_low    = (log_df["Alert Level"] == "LOW").sum()
    count_safe   = (log_df["Alert Level"] == "SAFE").sum()

    lc1, lc2, lc3, lc4, lc5 = st.columns(5)
    lc1.metric("Packets Processed", len(log_df))
    lc2.metric("🔴 HIGH ALERTS",   count_high)
    lc3.metric("🟡 MEDIUM ALERTS", count_medium)
    lc4.metric("🔵 LOW ALERTS",    count_low)
    lc5.metric("🟢 SAFE CONDITIONS", count_safe)

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

    csv_bytes = log_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Telemetry Incident Log (CSV)",
        data=csv_bytes,
        file_name=f"iiot_incident_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
    )

    if st.button("🗑️ Clear Incident Log"):
        st.session_state.alert_log = []
        st.rerun()

# ─────────────────────────────────────────────────────────────────────────────
# Auto-refresh loop
# ─────────────────────────────────────────────────────────────────────────────

if auto_refresh:
    time.sleep(5)
    st.rerun()
