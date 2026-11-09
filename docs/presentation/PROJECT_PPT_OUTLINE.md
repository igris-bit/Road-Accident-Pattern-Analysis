# 🖥️ Project Presentation (PPT) Slide Deck Outline

**Project Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring  
**Course:** IIoT-3 | **Team:** 14 Members | **Team Leader:** Lovish Chauhan  

---

### Slide 1: Title Slide
* **Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring
* **Subtitle:** Intelligent Transportation Systems (ITS) & Closed-Loop Actuation
* **Team Leader:** Lovish Chauhan
* **Team Members:** 14 Members (Listed with roles)
* **Links:** GitHub Repository & Live App: [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/)

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

### Slide 11: Team Contributions by Branch — Core Architecture & Infrastructure (1/3)
* **1. Lovish Chauhan (Team Leader) — Branch: `Lovish` [High / Lead]**
  - Spearheaded overall system architecture, live deployment on Streamlit Cloud, and repository governance.
  - Built the **What-If ML Accident Severity & Risk Predictor** calibrated on all 20,000 empirical records.
  - Engineered the **Smart Highway Variable Message Sign (VMS)** overhead LED actuator with speed overrides.
  - Implemented **Level-1 Trauma Hospital Emergency CAD Dispatch** with real-time telematics and ETAs.
  - Refactored codebase: removed redundant `app.py` and standardized production strictly on `streamlit_app.py`.
  - Built Windows `run_app.bat` one-click launcher and configured `.vscode` workspace environment for the team.
* **2. Krishu Kumar — Branch: `krishu` [High]**
  - Authored the foundational Streamlit dashboard application (commits `fca04dc`, `fd8d996`).
  - Integrated the initial Indian Roads Dataset (20,000 records) into the data pipeline.
  - Authored the Google Colab exploratory research notebook (`98f279f`).
  - Configured Linux system packages (`packages.txt`) and unpinned Streamlit dependencies (`de73c83`, `14f71a2`).
* **3. Mayank Gupta — Branch: `mayank` / `mayankgupta82357-crypto-patch-1` [High]**
  - Added the foundational IoT Simulation & Alert Monitoring module (commit `269d0c1`).
  - Created initial `iot_simulator.py` sensor generator and `pages/iot_monitor.py`.
  - Integrated Pydeck and Numpy requirements for geospatial hotspot plotting.
  - Contributed layout restructuring and patch synchronization (`2f38c7e`).
* **4. Alok Chaubey — Branch: `alok` [High]**
  - Resolved syntax errors and deduplicated sensor generator functions (commit `5f14dde`).
  - Synchronized state variables between `streamlit_app.py` and multi-page components.
  - Added the official Dev Container environment configuration (`e5dfaf4`).
  - Managed Pull Request #8 integration into origin.

---

### Slide 12: Team Contributions by Branch — Analytics & Feature Modules (2/3)
* **5. Arvind Mourya — Branch: `arvind` / `ayush-road-accident-analysis` [High]**
  - Implemented the **State-Wise Accident Analysis** module (commit `567d35e`).
  - Built grouping aggregations calculating accident volume and casualties for Top 10 Indian states.
  - Integrated dual bar charts comparing state frequencies and casualty ratios.
  - Conducted data validation on state-level accident tallies.
* **6. Amit Kohli — Commit: `c8f4245` [High]**
  - Engineered the **Accident Risk & Safety Insights** dashboard banner (commit `c8f4245`).
  - Added threshold-based visual alerts: High Risk ($\ge 0.7$), Moderate ($\ge 0.4$), and Lower Risk.
  - Implemented adverse weather keyword counters (rain, fog, storm) for road safety advisories.
  - Formulated descriptive safety recommendations for traffic management.
* **7. Ayush Patel — Branch: `ayush` / `ayush-road-accident-analysis` [High]**
  - Managed Pull Request #4 integration into the repository (commit `c108d2c`).
  - Synchronized updates to `streamlit_app.py` (commit `396683d`).
  - Contributed project setup instructions and feature descriptions in `README.md` (`2c3227a`).
  - Addressed dataset column formatting and peak-hour validation.
* **8. Pritam Kumar (Athox-X) — Branch: `pritam` / `kritikaaa` [Medium]**
  - Enhanced `iot_simulator.py` sensor generator methods (commit `0aa5a8d`).
  - Refined `pages/iot_monitor.py` alert display cards and UI styling (commit `03be2bc`).
  - Supported multi-page navigation routing and session persistence.
  - Conducted parameter checks on simulated weather conditions.

---

### Slide 13: Team Contributions by Branch — Engineering, Mapping & Docs (3/3)
* **9. Kritika — Branch: `kritikaaa` / `krtika` [Medium]**
  - Authored `CONTRIBUTING.md` team setup guide (commit `17c34b4`).
  - Verified IoT simulation telemetry parameters and supported documentation.
* **10. Sunal — Branch: `sunal` / `sunal914917-rgb-patch-1` [Medium]**
  - Updated `iot_monitor.py` parameters (commit `b54a36b`).
  - Authored multiple `README.md` documentation iterations (`f81277d`, `82a8fdd`, `fff9bae`).
* **11. Daniyal Malik — Branch: `Daniyal` [Medium]**
  - Standardized research notebook filename to `Road_Accident_Pattern_Analysis.ipynb` and updated references (commit `3758353`).
  - Conducted dataset schema verification.
* **12. Riddhi Gupta — Branch: `Riddhi-Gupta` [Medium]**
  - Documented project feature overviews in `README.md` (commits `91db893`, `bad32ef`).
  - Researched empirical accident patterns and environmental hazard factors in Indian cities.
* **13. Ayan Ansari — Branch: `ayan` [Low / Partial]**
  - Managed PR #3 merge from Krishu (commit `434d47e`).
  - Contributed to deployment documentation updates in `README.md` (`d6668d4`).
* **14. Om — Branch: `om` [Low / Minimal]**
  - Participated in peer code review cycles, tested sidebar filter widgets, and assisted in UI responsiveness verification.

---

### Slide 14: System Results & Real-World Impact
* **Empirical Hazard Findings:**
  - Dense winter fog combined with night hours (21:00–05:00) increases fatality probability by **+42%**.
  - Highways account for **2.3× higher casualty-per-accident severity** compared to urban roads, validating the need for dynamic VMS speed intervention.
* **Intelligent Transportation Impact:**
  - Dynamic VMS speed dampening (reducing limits to 35–40 km/h) mitigates multi-vehicle pileups during adverse weather.
  - Replaces static, unheeded signposts with active, condition-triggered electronic guidance.
* **Golden Hour Emergency Response:**
  - Computer-Aided Dispatch (CAD) routing calculates nearest Level-1 trauma centers with **5–8 min ambulance ETAs**.
  - Drastically cuts response lag, directly improving survival odds for critically injured highway commuters.

---

### Slide 15: Conclusion & Future Scope
* **Key Achievements:** Delivered a fully deployed, zero-error Streamlit Cloud application integrating descriptive analytics with real-time IIoT actuation.
* **Future Work:**
  - Hardware integration with ESP32/Raspberry Pi and LoRaWAN gateways.
  - YOLOv8 computer vision CCTV crash detection.
  - Vehicle-to-Infrastructure (V2I) connected vehicle warnings.
* **Q&A:** Open for questions from evaluators.

