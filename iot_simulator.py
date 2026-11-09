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
    temperature     = random.randint(10, 43)
    traffic_density = random.choice(TRAFFIC_DENSITY)
    road_type       = random.choice(ROAD_TYPES)
    lanes           = random.randint(2, 6)
    traffic_signal  = random.randint(0, 1)

    base_lat, base_lon = CITY_COORDINATES.get(chosen_city, (20.0, 78.0))
    latitude  = round(base_lat + random.uniform(-0.08, 0.08), 6)
    longitude = round(base_lon + random.uniform(-0.08, 0.08), 6)

    # Simulated vehicle average speed (km/h) for IoT telemetry
    base_speed = 80 if road_type == "highway" else (45 if road_type == "urban" else 60)
    if traffic_density == "high":
        base_speed -= 25
    if weather in ["rain", "fog"] or visibility == "low":
        base_speed -= 15
    avg_speed = max(15, base_speed + random.randint(-8, 12))

    risk = _compute_risk_score(
        weather, visibility, temperature, traffic_density,
        is_peak_hour, hour, road_type
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
        "avg_speed":       avg_speed,
        "risk_score":      risk,
    }


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
# Alert Rule Engine
# ─────────────────────────────────────────────────────────────────────────────

def evaluate_alert(reading: dict) -> dict:
    """
    Apply rule-based checks to a sensor reading and return an alert dict.
    Alert levels: "HIGH" | "MEDIUM" | "LOW" | "SAFE"
    """
    alerts = []
    level  = "SAFE"
    r = reading

    # Rule 1: Fog + low visibility + night
    if r["weather"] == "fog" and r["visibility"] == "low" and (r["hour"] >= 21 or r["hour"] <= 6):
        alerts.append("🌫️ Dense fog with critically low visibility during dark hours!")
        level = _escalate(level, "HIGH")

    # Rule 2: High risk score threshold
    if r["risk_score"] >= RISK_HIGH:
        alerts.append(f"🔴 Sensor computed risk score {r['risk_score']:.2f} exceeds HIGH threshold ({RISK_HIGH})")
        level = _escalate(level, "HIGH")

    # Rule 3: Rain + high traffic on highway
    if r["weather"] == "rain" and r["road_type"] == "highway" and r["traffic_density"] == "high":
        alerts.append("🌧️ Heavy rain on high-speed highway corridor with dense traffic")
        level = _escalate(level, "HIGH")

    # Rule 4: Medium risk score
    if RISK_MEDIUM <= r["risk_score"] < RISK_HIGH:
        alerts.append(f"🟡 Risk score {r['risk_score']:.2f} is in elevated MEDIUM range")
        level = _escalate(level, "MEDIUM")

    # Rule 5: Low visibility
    if r["visibility"] == "low" and level == "SAFE":
        alerts.append("⚠️ Poor roadside visibility detected by optical sensors")
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

    if not alerts:
        alerts.append("✅ Normal driving conditions — no hazardous patterns detected")

    return {
        "level":    level,
        "messages": alerts,
        "emoji":    {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🔵", "SAFE": "🟢"}[level],
        "color":    {"HIGH": "#FF4B4B", "MEDIUM": "#FFA500", "LOW": "#4B9EFF", "SAFE": "#21BA45"}[level],
    }


def _escalate(current: str, new: str) -> str:
    """Escalate alert priority."""
    order = {"SAFE": 0, "LOW": 1, "MEDIUM": 2, "HIGH": 3}
    return new if order[new] > order[current] else current


# ─────────────────────────────────────────────────────────────────────────────
# Smart Highway Actuator: Variable Message Sign (VMS) Simulation
# ─────────────────────────────────────────────────────────────────────────────

def get_vms_actuator_display(reading: dict, alert: dict) -> Dict[str, Any]:
    """
    Simulate an industrial Variable Message Sign (VMS) electronic overhead billboard.
    """
    level = alert["level"]
    weather = reading["weather"]
    road_type = reading["road_type"].upper()

    if level == "HIGH":
        speed_limit = 35 if weather == "fog" else 40
        return {
            "sign_title": "⚠️ CRITICAL HAZARD ALERT ⚠️",
            "line_1": f"ADVERSE {weather.upper()} CONDITIONS DETECTED",
            "line_2": f"MANDATORY SPEED LIMIT: {speed_limit} KM/H",
            "line_3": "INCREASE HEADWAY | HAZARD LIGHTS ON",
            "speed_limit": speed_limit,
            "led_color": "#FF3333",
            "status_text": "ACTIVE OVERRIDE (IIoT Triggered)",
            "sign_bg": "#110000",
        }
    elif level == "MEDIUM":
        speed_limit = 50
        return {
            "sign_title": "CAUTION: ELEVATED RISK ZONE",
            "line_1": f"{weather.upper()} / {reading['visibility'].upper()} VISIBILITY",
            "line_2": f"ADVISORY SPEED: {speed_limit} KM/H",
            "line_3": "KEEP SAFE DISTANCE | DO NOT OVERTAKE",
            "speed_limit": speed_limit,
            "led_color": "#FFAA00",
            "status_text": "ADVISORY BROADCAST",
            "sign_bg": "#151100",
        }
    elif level == "LOW":
        speed_limit = 65
        return {
            "sign_title": f"TRAFFIC ADVISORY — {road_type}",
            "line_1": "HEAVY TRAFFIC CONGESTION AHEAD",
            "line_2": f"RECOMMENDED SPEED: {speed_limit} KM/H",
            "line_3": "STAY IN LANE | EXPECT COMMUTE DELAYS",
            "speed_limit": speed_limit,
            "led_color": "#3399FF",
            "status_text": "INFORMATIONAL BROADCAST",
            "sign_bg": "#001122",
        }
    else:
        speed_limit = 80 if reading["road_type"] == "highway" else 50
        return {
            "sign_title": f"CORRIDOR CLEAR — {reading['city'].upper()}",
            "line_1": "OPTIMAL WEATHER & VISIBILITY",
            "line_2": f"REGULAR SPEED LIMIT: {speed_limit} KM/H",
            "line_3": "FOLLOW LANE DISCIPLINE | DRIVE SAFELY",
            "speed_limit": speed_limit,
            "led_color": "#00FF66",
            "status_text": "NORMAL OPERATIONS",
            "sign_bg": "#001a0d",
        }


# ─────────────────────────────────────────────────────────────────────────────
# Automated Emergency Dispatch (CAD) Simulation
# ─────────────────────────────────────────────────────────────────────────────

def get_emergency_dispatch_status(reading: dict, alert: dict) -> Dict[str, Any]:
    """
    Simulate Computer-Aided Emergency Dispatch (CAD) for roadside incidents.
    """
    city = reading["city"]
    services = CITY_EMERGENCY_SERVICES.get(city, {
        "hospital": "City Civil Trauma Hospital",
        "police_unit": "Regional Highway Patrol Unit",
        "dispatch_zone": "Main Arterial Corridor",
    })

    is_high = (alert["level"] == "HIGH")
    distance_km = round(random.uniform(1.8, 5.2), 1)
    eta_mins = int(distance_km * 2.5) + random.randint(1, 4)

    return {
        "activated": is_high,
        "status": "DISPATCHED / ACTIVE SOS" if is_high else "STANDBY / MONITORING",
        "hospital": services["hospital"],
        "hospital_dist": f"{distance_km} km",
        "police_unit": services["police_unit"],
        "dispatch_zone": services["dispatch_zone"],
        "ambulance_id": f"EMRI-108-{city[:3].upper()}-{random.randint(101, 899)}",
        "police_id": f"HP-PCR-{random.randint(11, 89)}",
        "eta": f"{eta_mins} mins" if is_high else "N/A",
        "channel": "MQTT / CAD Emergency Interconnect",
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
