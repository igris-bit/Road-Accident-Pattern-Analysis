"""
iot_simulator.py
----------------
IoT Simulation Engine For Road Accident Pattern Analysis.

This module provides:
  - Simulated IoT roadside sensor readings grounded in the Indian Roads Dataset.
  - Rule-based hazard alert evaluation.
  - Smart Highway Variable Message Sign (VMS) actuator simulation.
  - Automated Emergency Dispatch (CAD) simulation for metropolitan corridors.
  - Historical accident stats helper from the real dataset.
  - Empirical probabilistic accident severity prediction based on 20,000 records.
"""

import random
import datetime
from typing import Optional, Dict, Any
import pandas as pd
import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# Constants derived strictly from indian_roads_dataset.csv
# ─────────────────────────────────────────────────────────────────────────────

CITIES = [
    "Bangalore", "Chandigarh", "Chennai", "Delhi",
    "Hyderabad", "Kolkata", "Mumbai", "Pune",
]

WEATHER_CONDITIONS = ["clear", "fog", "rain"]
VISIBILITY_LEVELS  = ["low", "medium", "high"]
TRAFFIC_DENSITY    = ["low", "medium", "high"]
ROAD_TYPES         = ["highway", "rural", "urban"]
CAUSES             = ["weather", "distraction", "overspeeding", "drunk driving", "poor road"]
ACCIDENT_SEVERITY  = ["minor", "major", "fatal"]

# Alert level thresholds
RISK_HIGH   = 0.70
RISK_MEDIUM = 0.45

# Additional IoT Sensor Fields (compatible with Dev Container & extension branches)
VEHICLE_SPEED_RANGE = (0, 140)  # Speed in km/h
ROAD_CONDITIONS     = ["dry", "wet", "damaged", "slippery"]
SENSOR_STATUS       = ["online", "offline", "faulty"]

# Base coordinates for the 8 cities in the dataset
CITY_COORDINATES = {
    "Bangalore":  (12.9716, 77.5946),
    "Chandigarh": (30.7333, 76.7794),
    "Chennai":    (13.0827, 80.2707),
    "Delhi":      (28.6139, 77.2090),
    "Hyderabad":  (17.3850, 78.4867),
    "Kolkata":    (22.5726, 88.3639),
    "Mumbai":     (19.0760, 72.8777),
    "Pune":       (18.5204, 73.8567),
}

# Dedicated Emergency Infrastructure for each corridor in the dataset
CITY_EMERGENCY_SERVICES = {
    "Bangalore": {
        "hospital": "Victoria Hospital Trauma Care Centre",
        "police_unit": "Bangalore Traffic Command Unit 04",
        "dispatch_zone": "Central Corridor (Hosur Rd / Outer Ring)",
    },
    "Chandigarh": {
        "hospital": "PGIMER Level-1 Apex Trauma Centre",
        "police_unit": "Chandigarh Highway Patrol PCR-12",
        "dispatch_zone": "Madhya Marg - Tribune Chowk Corridor",
    },
    "Chennai": {
        "hospital": "Rajiv Gandhi Govt General Hospital",
        "police_unit": "Greater Chennai Traffic Police Unit 08",
        "dispatch_zone": "Anna Salai - Guindy Arterial Belt",
    },
    "Delhi": {
        "hospital": "AIIMS Jai Prakash Narayan Apex Trauma Centre",
        "police_unit": "Delhi Traffic Police Interceptor 02",
        "dispatch_zone": "Ring Road - DND Expressway Zone",
    },
    "Hyderabad": {
        "hospital": "Osmania General Hospital Trauma Wing",
        "police_unit": "Cyberabad Traffic Patrol Unit 09",
        "dispatch_zone": "Outer Ring Road (ORR) Gachibowli",
    },
    "Kolkata": {
        "hospital": "SSKM Hospital Trauma Care Facility",
        "police_unit": "Kolkata Traffic Police Lalbazar PCR",
        "dispatch_zone": "EM Bypass - Park Circus Connector",
    },
    "Mumbai": {
        "hospital": "KEM Hospital Emergency & Trauma Care",
        "police_unit": "Mumbai Traffic Police Western Express Interceptor",
        "dispatch_zone": "WEH - Bandra Reclamation Expressway",
    },
    "Pune": {
        "hospital": "Sassoon General Hospital Trauma Centre",
        "police_unit": "Pune City Traffic Branch - Unit 05",
        "dispatch_zone": "Mumbai-Pune Bypass (Warje-Katraj)",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# Sensor Reading Generator
# ─────────────────────────────────────────────────────────────────────────────

def generate_sensor_reading(city: Optional[str] = None) -> dict:
    """
    Simulate one IoT sensor reading from a roadside monitoring unit.
    Returns fields grounded in indian_roads_dataset.csv distributions.
    """
    now = datetime.datetime.now()

    chosen_city  = city if city in CITIES else random.choice(CITIES)
    hour         = now.hour
    is_weekend   = 1 if now.weekday() >= 5 else 0
    is_peak_hour = 1 if hour in range(8, 11) or hour in range(17, 21) else 0

    weather         = random.choice(WEATHER_CONDITIONS)
    visibility      = random.choice(VISIBILITY_LEVELS)
    traffic_density = random.choice(TRAFFIC_DENSITY)
    road_type       = random.choice(ROAD_TYPES)
    lanes           = random.choice([2, 4, 6]) if road_type == "highway" else random.choice([1, 2, 4])
    traffic_signal  = 0 if road_type == "highway" else random.choice([0, 1])

    # Seasonal and ambient temperature ranges (°C)
    if weather == "rain":
        temperature = random.randint(18, 30)
    elif weather == "fog":
        temperature = random.randint(8, 18)
    else:
        temperature = random.randint(22, 43)

    # Average corridor vehicle speed (km/h) based on conditions
    base_speed = 85 if road_type == "highway" else (45 if road_type == "urban" else 55)
    if weather == "fog":
        base_speed -= 30
    elif weather == "rain":
        base_speed -= 15
    if traffic_density == "high":
        base_speed -= 25

    avg_speed = max(15, min(120, int(random.gauss(base_speed, 8))))

    # Additional IoT sensor fields
    vehicle_speed  = avg_speed
    road_condition = "wet" if weather == "rain" else ("slippery" if weather == "fog" else "dry")
    sensor_status  = "online"

    # Precise GPS latitude & longitude near the chosen corridor
    base_lat, base_lon = CITY_COORDINATES.get(chosen_city, (20.5937, 78.9629))
    latitude  = round(base_lat + random.uniform(-0.06, 0.06), 4)
    longitude = round(base_lon + random.uniform(-0.06, 0.06), 4)

    # Calculate empirical heuristic risk score
    risk = _compute_risk_score(
        weather=weather,
        visibility=visibility,
        temperature=temperature,
        traffic_density=traffic_density,
        is_peak_hour=is_peak_hour,
        hour=hour,
        road_type=road_type
    )

    return {
        "timestamp":       now.strftime("%Y-%m-%d %H:%M:%S"),
        "city":            chosen_city,
        "latitude":        latitude,
        "longitude":       longitude,
        "weather":         weather,
        "visibility":      visibility,
        "temperature":     temperature,
        "traffic_density": traffic_density,
        "road_type":       road_type,
        "lanes":           lanes,
        "traffic_signal":  traffic_signal,
        "hour":            hour,
        "is_weekend":      is_weekend,
        "is_peak_hour":    is_peak_hour,
        "avg_speed":       avg_speed,
        "vehicle_speed":   vehicle_speed,
        "road_condition":  road_condition,
        "sensor_status":   sensor_status,
        "day_of_week":     now.strftime("%A"),
        "risk_score":      risk,
    }


def evaluate_risk(accident_probability: float) -> str:
    """Classify accident risk probability into warning levels."""
    if accident_probability >= RISK_HIGH:
        return "HIGH RISK - Emergency Alert"
    elif accident_probability >= RISK_MEDIUM:
        return "MEDIUM RISK - Warning"
    else:
        return "LOW RISK - Normal"


def simulate_accident_risk(accident_probability: Optional[float] = None, city: Optional[str] = None) -> dict:
    """Generate a complete simulation result combining sensor readings and alert classification."""
    if accident_probability is None:
        accident_probability = random.random()

    accident_probability = max(0.0, min(1.0, accident_probability))
    reading = generate_sensor_reading(city=city)
    reading["accident_probability"] = round(accident_probability, 2)
    reading["emergency_alert"] = evaluate_risk(accident_probability)
    return reading


def _compute_risk_score(weather, visibility, temperature,
                        traffic_density, is_peak_hour, hour, road_type="highway") -> float:
    """Heuristic risk score in [0, 1] aligned with the dataset distributions."""
    score = 0.0

    score += {"clear": 0.05, "rain": 0.28, "fog": 0.38}.get(weather, 0.10)
    score += {"high": 0.0, "medium": 0.12, "low": 0.26}.get(visibility, 0.10)
    score += {"low": 0.0, "medium": 0.10, "high": 0.22}.get(traffic_density, 0.05)
    score += {"highway": 0.10, "rural": 0.08, "urban": 0.05}.get(road_type, 0.05)

    if hour >= 22 or hour <= 5:
        score += 0.16
    if is_peak_hour:
        score += 0.08
    if temperature >= 42 or temperature <= 9:
        score += 0.08

    score += random.uniform(-0.04, 0.04)
    return round(max(0.05, min(0.98, score)), 2)


# ─────────────────────────────────────────────────────────────────────────────
# Rule-Based Alert Evaluation Engine
# ─────────────────────────────────────────────────────────────────────────────

def evaluate_alert(reading: dict) -> dict:
    """
    Evaluate multi-factor highway safety rules against the simulated reading.
    Returns alert priority, alert messages, and actionable recommendations.
    """
    alerts = []
    level  = "SAFE"
    r      = reading

    # Rule 1: Dense fog hazard
    if r["weather"] == "fog" and r["visibility"] == "low":
        alerts.append("🌫️ CRITICAL: Dense Fog & Low Visibility — Extreme collision hazard")
        level = _escalate(level, "HIGH")
    elif r["weather"] == "fog":
        alerts.append("🌫️ Moderate Fog detected — Reduce speed and use low-beam headlights")
        level = _escalate(level, "MEDIUM")

    # Rule 2: Heavy precipitation hazard
    if r["weather"] == "rain" and r["traffic_density"] == "high":
        alerts.append("🌧️ Heavy Rain with High Traffic Density — High hydroplaning risk")
        level = _escalate(level, "HIGH")
    elif r["weather"] == "rain":
        alerts.append("🌧️ Wet Highway Pavement — Increase vehicle following distance")
        level = _escalate(level, "MEDIUM")

    # Rule 3: Highway speed vs visibility mismatch
    if r["road_type"] == "highway" and r["visibility"] == "low" and r.get("avg_speed", 0) > 60:
        alerts.append("🏎️ Overspeeding during low visibility — Severe pileup danger")
        level = _escalate(level, "HIGH")

    # Rule 4: Nighttime driving risk
    if (r["hour"] >= 22 or r["hour"] <= 5) and r["weather"] in ["fog", "rain"]:
        alerts.append("🌙 Hazardous Late-Night Weather — Heightened collision probability")
        level = _escalate(level, "HIGH")

    # Rule 5: Multi-factor risk threshold
    if r["risk_score"] >= RISK_HIGH:
        alerts.append(f"⚠️ Extreme Corridor Risk Score ({r['risk_score']:.2f} >= {RISK_HIGH})")
        level = _escalate(level, "HIGH")
    elif r["risk_score"] >= RISK_MEDIUM:
        alerts.append(f"⚠️ Elevated Corridor Risk Score ({r['risk_score']:.2f})")
        level = _escalate(level, "MEDIUM")

    # Rule 6: Extreme temperature
    if r["temperature"] >= 42:
        alerts.append(f"🌡️ Extreme temperature ({r['temperature']}°C) — elevated risk of tyre blowouts")
        level = _escalate(level, "MEDIUM")
    elif r["temperature"] <= 10:
        alerts.append(f"❄️ Cold temperature ({r['temperature']}°C) — low tyre grip / moisture condensation")
        level = _escalate(level, "MEDIUM")

    # Rule 7: Peak hour congestion
    if r["is_peak_hour"] and r["traffic_density"] == "high" and level == "SAFE":
        alerts.append("🚦 Heavy peak-hour commuter congestion detected")
        level = _escalate(level, "LOW")

    # Rule 8: High vehicle speed check
    if r.get("vehicle_speed", 0) >= 100:
        alerts.append(f"🏎️ High vehicle speed ({r['vehicle_speed']} km/h) — overspeeding hazard")
        level = _escalate(level, "MEDIUM")

    # Rule 9: Hazardous road surface
    if r.get("road_condition") in ["slippery", "damaged"]:
        alerts.append(f"⚠️ Road surface condition is {r['road_condition']} — reduced traction hazard")
        level = _escalate(level, "MEDIUM")

    if not alerts:
        alerts.append("✅ Normal driving conditions — no hazardous patterns detected")

    return {
        "level":    level,
        "emoji":    {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🔵", "SAFE": "🟢"}[level],
        "messages": alerts,
        "count":    len(alerts),
    }


def _escalate(current: str, candidate: str) -> str:
    """Escalate alert priority: SAFE < LOW < MEDIUM < HIGH"""
    order = ["SAFE", "LOW", "MEDIUM", "HIGH"]
    return candidate if order.index(candidate) > order.index(current) else current


# ─────────────────────────────────────────────────────────────────────────────
# Dynamic Variable Message Sign (VMS) Overhead Actuator
# ─────────────────────────────────────────────────────────────────────────────

def get_vms_speed_advisory(reading: dict, alert: dict) -> dict:
    """
    Computes real-time dynamic speed dampening and electronic billboard text
    for overhead Highway Variable Message Signs (VMS).
    """
    level = alert["level"]
    weather = reading["weather"]
    road_type = reading["road_type"]

    default_limit = 80 if road_type == "highway" else (50 if road_type == "urban" else 60)

    if level == "HIGH":
        enforced_limit = 35 if weather == "fog" else 40
        action = "CRITICAL HAZARD SPEED OVERRIDE"
        icon = "🛑"
        warning = "MANDATORY REDUCE SPEED • HEAVY FOG/RAIN AHEAD"
        sub_msg = "KEEP SAFE HEADWAY • TURN ON HAZARDS"
    elif level == "MEDIUM":
        enforced_limit = 50 if road_type == "highway" else 40
        action = "ADVISORY SPEED REDUCTION"
        icon = "⚠️"
        warning = "CAUTION: ADVERSE WEATHER DETECTED"
        sub_msg = "WET ROAD SURFACE • NO OVERTAKING"
    elif level == "LOW":
        enforced_limit = default_limit - 10
        action = "CONGESTION FLOW ADVISORY"
        icon = "🔵"
        warning = "HEAVY TRAFFIC FLOW DETECTED"
        sub_msg = "MAINTAIN LANE DISCIPLINE"
    else:
        enforced_limit = default_limit
        action = "NORMAL HIGHWAY OPERATION"
        icon = "🟢"
        warning = "ALL LANES CLEAR • DRIVE SAFELY"
        sub_msg = "STANDARD HIGHWAY SPEED LIMIT APPLIES"

    return {
        "default_limit": default_limit,
        "enforced_limit": enforced_limit,
        "speed_reduction": default_limit - enforced_limit,
        "action": action,
        "icon": icon,
        "primary_warning": warning,
        "secondary_message": sub_msg,
        "road_type": road_type.upper(),
    }


def get_vms_actuator_display(reading: dict, alert: dict) -> dict:
    """
    Formats the LED matrix visual attributes for the simulated overhead VMS display.
    """
    advisory = get_vms_speed_advisory(reading, alert)
    level = alert["level"]

    if level == "HIGH":
        led_color = "#FF3333"
        sign_bg   = "#1A0000"
        title     = "⚠️ DANGER: HIGH ACCIDENT HAZARD ⚠️"
    elif level == "MEDIUM":
        led_color = "#FFAA00"
        sign_bg   = "#1A1000"
        title     = "⚠️ CAUTION: ADVISORY WARNING ⚠️"
    elif level == "LOW":
        led_color = "#3399FF"
        sign_bg   = "#001020"
        title     = "ℹ️ TRAFFIC INFORMATION NOTICE ℹ️"
    else:
        led_color = "#00FF66"
        sign_bg   = "#001A0A"
        title     = "✅ SMART HIGHWAY CORRIDOR NORMAL ✅"

    line_1 = advisory["primary_warning"]
    line_2 = f"SPEED LIMIT: {advisory['enforced_limit']} KM/H  (REDUCED FROM {advisory['default_limit']} KM/H)"
    line_3 = advisory["secondary_message"]

    return {
        "led_color": led_color,
        "sign_bg": sign_bg,
        "sign_title": title,
        "line_1": line_1,
        "line_2": line_2,
        "line_3": line_3,
        "status_text": f"{advisory['action']} [{reading['city'].upper()}]"
    }


# ─────────────────────────────────────────────────────────────────────────────
# Automated Emergency CAD Dispatch System
# ─────────────────────────────────────────────────────────────────────────────

def get_emergency_dispatch(reading: dict, alert: dict) -> dict:
    """
    Simulates automated Computer-Aided Dispatch (CAD) routing emergency
    ambulances and police units during high-risk conditions.
    """
    city = reading["city"]
    emergency_meta = CITY_EMERGENCY_SERVICES.get(city, {
        "hospital": "Regional Apex Trauma Centre",
        "police_unit": "National Highway Patrol Command",
        "dispatch_zone": f"{city} Metropolitan Arterial Belt",
    })

    level = alert["level"]
    is_dispatched = level in ["HIGH", "MEDIUM"]

    ambulance_id = f"ALS-{city[:3].upper()}-{random.randint(101, 899)}"
    police_car   = f"PATROL-{city[:3].upper()}-{random.randint(11, 88)}"
    eta_mins     = random.randint(5, 8) if level == "HIGH" else random.randint(9, 14)

    return {
        "is_active": is_dispatched,
        "severity_level": level,
        "hospital_name": emergency_meta["hospital"],
        "police_unit": emergency_meta["police_unit"],
        "dispatch_zone": emergency_meta["dispatch_zone"],
        "assigned_ambulance": ambulance_id,
        "assigned_police": police_car,
        "estimated_arrival_minutes": eta_mins,
        "coordinates": (reading["latitude"], reading["longitude"]),
        "dispatch_timestamp": reading["timestamp"],
    }


# ─────────────────────────────────────────────────────────────────────────────
# Historical Stats Helper
# ─────────────────────────────────────────────────────────────────────────────

def get_city_historical_stats(df: pd.DataFrame, city: str) -> dict:
    """
    Pull accident statistics for a given city from the real dataset.
    """
    city_df = df[df["city"] == city]

    if city_df.empty:
        return {"found": False, "city": city}

    total       = len(city_df)
    fatal       = len(city_df[city_df["accident_severity"] == "fatal"])
    major       = len(city_df[city_df["accident_severity"] == "major"])
    avg_risk    = round(city_df["risk_score"].mean(), 3)
    top_cause   = city_df["cause"].value_counts().idxmax() if "cause" in city_df.columns else "N/A"
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


# ─────────────────────────────────────────────────────────────────────────────
# Empirical Severity Predictor Grounded in the 20,000 Records
# ─────────────────────────────────────────────────────────────────────────────

def predict_accident_severity(df: pd.DataFrame, city: str, weather: str,
                              visibility: str, road_type: str, traffic_density: str,
                              hour: int, vehicles_involved: int) -> Dict[str, Any]:
    """
    Probabilistic accident severity & risk prediction directly estimated
    from historical data in indian_roads_dataset.csv.
    """
    if df.empty:
        return {
            "predicted_severity": "minor",
            "probabilities": {"minor": 60.0, "major": 30.0, "fatal": 10.0},
            "risk_score": 0.40,
            "risk_level": "Moderate",
        }

    # Filter with progressive relaxation (Bayesian smoothing)
    subset = df[
        (df["weather"] == weather) &
        (df["road_type"] == road_type) &
        (df["visibility"] == visibility)
    ]

    if len(subset) < 30:
        subset = df[(df["weather"] == weather) | (df["visibility"] == visibility)]

    if subset.empty:
        subset = df

    # Calculate baseline frequencies
    counts = subset["accident_severity"].value_counts(normalize=True).to_dict()
    p_minor = counts.get("minor", 0.50)
    p_major = counts.get("major", 0.35)
    p_fatal = counts.get("fatal", 0.15)

    # Heuristic adjustments for vehicle count & night hours
    if vehicles_involved >= 3:
        p_fatal *= 1.45
        p_major *= 1.25
        p_minor *= 0.65

    if hour >= 22 or hour <= 5:
        p_fatal *= 1.35
        p_major *= 1.15

    if traffic_density == "high" and weather in ["rain", "fog"]:
        p_major *= 1.20

    # Re-normalize to 100%
    total_weight = p_minor + p_major + p_fatal
    pct_minor = round((p_minor / total_weight) * 100, 1)
    pct_major = round((p_major / total_weight) * 100, 1)
    pct_fatal = round((p_fatal / total_weight) * 100, 1)

    probs = {"minor": pct_minor, "major": pct_major, "fatal": pct_fatal}
    predicted = max(probs, key=probs.get)

    # Composite risk score estimation
    est_risk = (pct_minor * 0.20 + pct_major * 0.55 + pct_fatal * 1.0) / 100
    est_risk = round(max(0.10, min(0.95, est_risk)), 2)

    risk_level = "High" if est_risk >= 0.70 else ("Moderate" if est_risk >= 0.45 else "Low")

    # Key contributing factors
    contributors = []
    if weather in ["fog", "rain"]:
        contributors.append(f"Adverse Weather ({weather.capitalize()})")
    if visibility == "low":
        contributors.append("Low Optical Visibility")
    if hour >= 22 or hour <= 5:
        contributors.append("Late-Night Hazardous Hours")
    if vehicles_involved >= 3:
        contributors.append(f"Multi-Vehicle Involvement ({vehicles_involved} vehicles)")
    if traffic_density == "high":
        contributors.append("Dense Highway Traffic")
    if not contributors:
        contributors.append("Optimal Corridor Baseline Conditions")

    return {
        "predicted_severity": predicted,
        "probabilities": probs,
        "risk_score": est_risk,
        "risk_level": risk_level,
        "contributors": contributors,
    }
