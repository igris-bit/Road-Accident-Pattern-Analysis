# 🖥️ Project Presentation (PPT) Slide Deck Outline

**Project Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring  
**Course:** IIoT-3 | **Team:** 14 Members | **Team Leader:** Lovish Chauhan  

---

### Slide 1: Title Slide
* **Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring
* **Subtitle:** Intelligent Transportation Systems (ITS) & Closed-Loop Actuation
* **Team Leader:** Lovish Chauhan
* **Team Members:** 14 Members (Listed with roles)
* **Links:** GitHub Repository & Live Streamlit App

---

### Slide 2: Problem Statement & Motivation
* **The Challenge:** Over 150,000 traffic fatalities annually in India; traditional retrospective analysis cannot prevent accidents before they occur.
* **The Gap:** Lack of real-time sensor integration connecting roadside environmental hazards to automated driver warnings and emergency dispatch.
* **Our Solution:** A hybrid platform combining **20,000 real accident records** with an **Industrial IoT (IIoT) edge simulation, dynamic VMS highway signs, and automated hospital CAD dispatch**.

---

### Slide 3: Dataset & Data Preprocessing
* **Source:** `indian_roads_dataset.csv` (20,000 empirical accident records).
* **Geographical Scope:** 8 major metropolitan corridors: *Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Pune*.
* **24 Core Features:** Spatial (Lat/Lon), Temporal (Hour, Weekend, Peak), Environmental (Weather, Visibility, Temp), Traffic (Density, Lanes, Signal), Severity (Minor, Major, Fatal).
* **Data Cleaning:** Deduplication, null imputation, dropping non-informative attributes (`festival`), coordinate standardization.

---

### Slide 4: 3-Tier Industrial IoT Architecture
* **Tier 1 — Perception Layer (Edge Sensing):** Optical visibility sensors, roadside weather stations, speed radar units, traffic counters.
* **Tier 2 — Network & Processing Layer:** IoT Gateway telemetry streaming (MQTT simulation), rule-based hazard engine, empirical Bayesian severity calculator.
* **Tier 3 — Application & Actuation Layer:** Streamlit Community Cloud UI, dynamic overhead Variable Message Signs (VMS), and automated CAD hospital routing.

---

### Slide 5: Historical Analytics Dashboard (Module 1)
* **Interactive Drill-Down:** Dynamic multi-factor filters by State, City, Severity, Road Type, and Weather.
* **Key Metric Indicators:** Total Accidents, Casualties, Fatal %, and Average Risk Index.
* **Top 10 States Ranking:** Bar chart comparisons correlating accident volume with casualty severity.
* **Summary Tables:** Percentage breakdown of environmental and temporal hazard factors.

---

### Slide 6: "What-If" AI Severity Predictor (Module 1)
* **What it does:** Allows highway operators to simulate hypothetical driving scenarios and receive instant accident severity probability distributions.
* **Inputs:** Scenario City, Weather (*Clear/Fog/Rain*), Visibility (*High/Med/Low*), Road Type (*Highway/Urban/Rural*), Hour of Day, Vehicles Involved.
* **Outputs:**
  - Predicted Severity: *Minor Incident*, *Major Collision*, or *Fatal Accident*.
  - Estimated Risk Index (0.00 – 1.00 scale).
  - Probability Breakdown (% Minor, % Major, % Fatal).
  - Automated Contributing Hazard Flags.

---

### Slide 7: IIoT Edge Telemetry & Hazard Engine (Module 2)
* **Telemetry Streaming:** Simulated live packet generation from roadside units (5-second auto-refresh option).
* **Rule-Based Hazard Escalation:**
  - `SAFE`: Optimal visibility and dry road conditions.
  - `LOW`: Peak-hour commuter traffic congestion.
  - `MEDIUM`: Low visibility, wet pavement, or extreme temperatures (>42°C / <10°C).
  - `HIGH`: Dense fog at night or heavy rain during highway peak hours.

---

### Slide 8: Smart Highway Variable Message Sign (VMS) Actuator
* **Closed-Loop Actuation:** Moves beyond passive data visualization to physical roadside safety intervention.
* **Overhead Electronic LED Billboard:** Styled with retro-illuminated matrix typography.
* **Dynamic Speed Limit Overrides:**
  - Normal conditions: 80 km/h.
  - Heavy rain/traffic: 50 km/h.
  - Critical fog/low visibility: Mandatory reduction to 35 km/h with hazard flasher advisory.

---

### Slide 9: Automated Emergency CAD Dispatch Interconnect
* **Computer-Aided Dispatch (CAD):** Automates emergency response within the critical "Golden Hour".
* **Corridor-Specific Trauma Hospitals:**
  - *Delhi:* AIIMS Apex Trauma Centre
  - *Mumbai:* KEM Hospital Emergency Unit
  - *Bangalore:* Victoria Hospital Trauma Care
  - *Chandigarh:* PGIMER Level-1 Trauma Wing
* **Telemetry Telematics:** Displays allocated ambulance unit ID, highway patrol cruiser, distance (km), and real-time ETA.

---

### Slide 10: Interactive Geospatial Hotspot Map
* **Pydeck GIS Mapping:** 3D interactive Scatterplot layer rendering historical accident blackspots across Indian metropolitan corridors.
* **Visual Severity Coding:** Blue (*Minor*), Orange (*Major*), Red (*Fatal*), and Green (*Active IoT Sensor Node*).
* **Audit Trail:** Session-based incident log with one-click timestamped CSV export for municipal audits.

---

### Slide 11: Team Workload Distribution (14 Members)
* **Squad 1 (Core Dashboard & UI):** Mayank Gupta, Pritam Kumar, Kritika
* **Squad 2 (Data Pipeline & EDA):** Ayush Patel, Krishu Kumar, Sunal, Daniyal Malik
* **Squad 3 (IIoT Simulation & Actuation):** Lovish Chauhan (Lead), Arvind Mourya, Amit Kohli
* **Squad 4 (GIS Mapping & Research):** Riddhi Gupta, Alok, Ayan, Om

---

### Slide 12: Conclusion & Future Scope
* **Key Achievements:** Delivered a fully deployed, zero-error Streamlit Cloud application integrating descriptive analytics with real-time IIoT actuation.
* **Future Work:**
  - Hardware integration with ESP32/Raspberry Pi and LoRaWAN gateways.
  - YOLOv8 computer vision CCTV crash detection.
  - Vehicle-to-Infrastructure (V2I) connected vehicle warnings.
* **Q&A:** Open for questions from evaluators.
