"""
iot_simulator.py
----------------
IoT Simulation Engine for Road Accident Pattern Analysis.

This module provides:
  - Simulated IoT sensor readings (no physical hardware required).
  - Rule-based alert evaluation using the same fields as the real dataset.
  - Helper to pull historical accident stats from the real CSV for a given city.

All randomness is seeded per-call so repeated calls give fresh readings.
"""

import random
import datetime
from typing import Optional
import pandas as pd

# ─────────────────────────────────────────────────────────────────────────────
# Constants derived from the real dataset's unique values
# ─────────────────────────────────────────────────────────────────────────────

CITIES = [
    "Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Chennai",
    "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Chandigarh",
    "Lucknow", "Bhopal", "Nagpur", "Kochi", "Indore",
]

WEATHER_CONDITIONS = ["clear", "rain", "fog"]
VISIBILITY_LEVELS  = ["low", "medium", "high"]
TRAFFIC_DENSITY    = ["low", "medium", "high"]
CAUSES             = ["weather", "distraction", "speeding", "drunk_driving", "poor_road"]
ROAD_TYPES         = ["highway", "city road", "rural road", "expressway"]

# Alert level thresholds
RISK_HIGH   = 0.70
RISK_MEDIUM = 0.45


# Additional IoT Sensor Fields
VEHICLE_SPEED_RANGE = (0, 140)  # Speed in km/h

ROAD_CONDITIONS = [
    "dry",
    "wet",
    "damaged",
    "slippery"
]

ACCIDENT_SEVERITY = [
    "low",
    "medium",
    "high"
]

SENSOR_STATUS = [
    "online",
    "offline",
    "faulty"
]

# Risk and Alert Thresholds
RISK_MEDIUM = 0.40
RISK_HIGH = 0.70

# Generate Simulated IoT Sensor Data
def generate_sensor_reading():
    return {
        "vehicle_speed": random.randint(*VEHICLE_SPEED_RANGE),
        "road_condition": random.choice(ROAD_CONDITIONS),
        "accident_severity": random.choice(ACCIDENT_SEVERITY),
        "sensor_status": random.choice(SENSOR_STATUS),
        "weather": random.choice(WEATHER_CONDITIONS),
        "visibility": random.choice(VISIBILITY_LEVELS),
        "traffic_density": random.choice(TRAFFIC_DENSITY),
        "timestamp": datetime.datetime.now().isoformat()
    }

# Evaluate Accident Risk and Generate Alert
def evaluate_risk(accident_probability):
    if accident_probability >= RISK_HIGH:
        return "HIGH RISK - Emergency Alert"
    elif accident_probability >= RISK_MEDIUM:
        return "MEDIUM RISK - Warning"
    else:
        return "LOW RISK - Normal"

# Generate a Complete Simulation Result
def simulate_accident_risk(accident_probability=None):
    if accident_probability is None:
        accident_probability = random.random()

    accident_probability = max(0.0, min(1.0, accident_probability))

    reading = generate_sensor_reading()
    reading["accident_probability"] = round(accident_probability, 2)
    reading["emergency_alert"] = evaluate_risk(accident_probability)

    return reading



# ─────────────────────────────────────────────────────────────────────────────
# Sensor Reading Generator
# ─────────────────────────────────────────────────────────────────────────────

def generate_sensor_reading(city: Optional[str] = None) -> dict:
    """
    Simulate one IoT sensor reading from a roadside unit.

    Returns a dict with the same field names used in the real CSV so that
    alert rules work identically on both real and simulated data.
    """
    now = datetime.datetime.now()

    chosen_city    = city if city else random.choice(CITIES)
    hour           = now.hour                                   # real current hour
    is_weekend     = 1 if now.weekday() >= 5 else 0

    is_peak_hour   = 1 if hour in range(8, 10) or hour in range(17, 20) else 0

    weather        = random.choice(WEATHER_CONDITIONS)
    visibility     = random.choice(VISIBILITY_LEVELS)
    temperature    = random.randint(8, 45)                      # °C, Indian range
    traffic_density = random.choice(TRAFFIC_DENSITY)
    road_type      = random.choice(ROAD_TYPES)
    lanes          = random.randint(1, 6)
    traffic_signal = random.randint(0, 1)

    # Simulate sensor lat/lon near the chosen city (rough offsets)
    base_coords = {
        "Mumbai": (19.07, 72.87), "Delhi": (28.61, 77.20),
        "Bengaluru": (12.97, 77.59), "Hyderabad": (17.38, 78.48),
        "Chennai": (13.08, 80.27), "Kolkata": (22.57, 88.36),
        "Pune": (18.52, 73.86), "Ahmedabad": (23.03, 72.57),
        "Jaipur": (26.91, 75.79), "Chandigarh": (30.74, 76.79),
        "Lucknow": (26.85, 80.95), "Bhopal": (23.26, 77.41),
        "Nagpur": (21.15, 79.09), "Kochi": (9.93, 76.26),
        "Indore": (22.72, 75.86),
    }
    base_lat, base_lon = base_coords.get(chosen_city, (20.0, 78.0))
    latitude  = round(base_lat  + random.uniform(-0.15, 0.15), 6)
    longitude = round(base_lon  + random.uniform(-0.15, 0.15), 6)

    # Compute a risk score using the same logic as the dataset (heuristic)
    risk = _compute_risk_score(
        weather, visibility, temperature, traffic_density,
        is_peak_hour, hour
    )

    return {
        "timestamp":       now.strftime("%Y-%m-%d %H:%M:%S"),
        "city":            chosen_city,
        "latitude":        latitude,
        "longitude":       longitude,
        "hour":            hour,
        "day_of_week":     now.strftime("%A"),
        "is_weekend":      is_weekend,
        "is_peak_hour":    is_peak_hour,
        "weather":         weather,
        "visibility":      visibility,
        "temperature":     temperature,
        "traffic_density": traffic_density,
        "road_type":       road_type,
        "lanes":           lanes,
        "traffic_signal":  traffic_signal,
        "risk_score":      risk,
    }


def _compute_risk_score(weather, visibility, temperature,
                        traffic_density, is_peak_hour, hour) -> float:
    """Heuristic risk score in [0, 1] based on sensor fields."""
    score = 0.0

    # Weather contribution
    score += {"clear": 0.05, "rain": 0.25, "fog": 0.40}.get(weather, 0.10)

    # Visibility contribution
    score += {"high": 0.0, "medium": 0.10, "low": 0.25}.get(visibility, 0.10)

    # Traffic contribution
    score += {"low": 0.0, "medium": 0.10, "high": 0.20}.get(traffic_density, 0.05)

    # Nighttime (22:00–05:00)
    if hour >= 22 or hour <= 5:
        score += 0.15

    # Peak hour
    if is_peak_hour:
        score += 0.10

    # Extreme temperature
    if temperature >= 42 or temperature <= 8:
        score += 0.10

    # Add small random noise so consecutive readings differ
    score += random.uniform(-0.05, 0.05)

    return round(max(0.0, min(1.0, score)), 2)


# ─────────────────────────────────────────────────────────────────────────────
# Alert Rule Engine
# ─────────────────────────────────────────────────────────────────────────────

def evaluate_alert(reading: dict) -> dict:
    """
    Apply rule-based checks to a sensor reading and return an alert dict.

    Alert levels: "HIGH" | "MEDIUM" | "LOW" | "SAFE"
    """
    alerts = []
    level  = "SAFE"

    r = reading  # shorthand

    # Rule 1: Fog + low visibility + nighttime → critical
    if r["weather"] == "fog" and r["visibility"] == "low" and (r["hour"] >= 22 or r["hour"] <= 5):
        alerts.append("🌫️ Dense fog with low visibility at night — extremely dangerous!")
        level = _escalate(level, "HIGH")

    # Rule 2: High risk score
    if r["risk_score"] >= RISK_HIGH:
        alerts.append(f"🔴 Risk score {r['risk_score']:.2f} exceeds HIGH threshold ({RISK_HIGH})")
        level = _escalate(level, "HIGH")

    # Rule 3: Rain + peak hour + high traffic
    if r["weather"] == "rain" and r["is_peak_hour"] and r["traffic_density"] == "high":
        alerts.append("🌧️ Heavy rain during peak hour with high traffic density")
        level = _escalate(level, "HIGH")

    # Rule 4: Medium risk score
    if RISK_MEDIUM <= r["risk_score"] < RISK_HIGH:
        alerts.append(f"🟡 Risk score {r['risk_score']:.2f} is in MEDIUM range")
        level = _escalate(level, "MEDIUM")

    # Rule 5: Low visibility (any condition)
    if r["visibility"] == "low" and level == "SAFE":
        alerts.append("⚠️ Low visibility detected on road")
        level = _escalate(level, "MEDIUM")

    # Rule 6: Extreme temperature
    if r["temperature"] >= 42:
        alerts.append(f"🌡️ Extreme heat ({r['temperature']}°C) — risk of tyre burst / driver fatigue")
        level = _escalate(level, "MEDIUM")
    elif r["temperature"] <= 8:
        alerts.append(f"❄️ Very cold ({r['temperature']}°C) — black ice / fog risk")
        level = _escalate(level, "MEDIUM")

    # Rule 7: Peak-hour congestion warning
    if r["is_peak_hour"] and r["traffic_density"] == "high" and level == "SAFE":
        alerts.append("🚦 Peak hour with high traffic — congestion warning")
        level = _escalate(level, "LOW")

    # No alerts triggered
    if not alerts:
        alerts.append("✅ Conditions are normal — no hazards detected")

    return {
        "level":    level,
        "messages": alerts,
        "emoji":    {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🔵", "SAFE": "🟢"}[level],
        "color":    {"HIGH": "#FF4B4B", "MEDIUM": "#FFA500", "LOW": "#4B9EFF", "SAFE": "#21BA45"}[level],
    }


def _escalate(current: str, new: str) -> str:
    """Only move the alert level UP, never down."""
    order = {"SAFE": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3}
    return new if order[new] > order[current] else current


# ─────────────────────────────────────────────────────────────────────────────
# Historical Stats Helper
# ─────────────────────────────────────────────────────────────────────────────

def get_city_historical_stats(df: pd.DataFrame, city: str) -> dict:
    """
    Pull accident statistics for a given city from the real dataset.
    Returns a dict of summary numbers useful for the IoT dashboard context panel.
    """
    city_df = df[df["city"] == city]

    if city_df.empty:
        return {"found": False, "city": city}

    total     = len(city_df)
    fatal     = len(city_df[city_df["accident_severity"] == "fatal"])
    major     = len(city_df[city_df["accident_severity"] == "major"])
    avg_risk  = round(city_df["risk_score"].mean(), 3)
    top_cause = city_df["cause"].value_counts().idxmax() if "cause" in city_df.columns else "N/A"
    top_weather = city_df["weather"].value_counts().idxmax()
    peak_hour   = int(city_df["hour"].value_counts().idxmax())

    return {
        "found":        True,
        "city":         city,
        "total":        total,
        "fatal":        fatal,
        "major":        major,
        "fatal_pct":    round(fatal / total * 100, 1) if total else 0,
        "avg_risk":     avg_risk,
        "top_cause":    top_cause,
        "top_weather":  top_weather,
        "peak_hour":    peak_hour,
    }
