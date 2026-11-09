# 🖥️ Project Presentation (PPT) — Concise 10-Slide Deck

**Project Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring  
**Course:** Industrial Internet of Things (IIoT-3)  
**Team Leader:** Lovish Chauhan (`lovishneeraj@gmail.com`)  
**Team Size:** 14 Members  
**🌐 Live Web App:** [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/)  
**GitHub Repository:** [https://github.com/igris-bit/Road-Accident-Pattern-Analysis](https://github.com/igris-bit/Road-Accident-Pattern-Analysis)  

---

### Slide 1: Title & Overview
* **Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring
* **Subtitle:** Closed-Loop Intelligent Transportation System (ITS) • Empirical AI Severity Prediction • Dynamic VMS Actuation
* **Course:** Industrial Internet of Things (IIoT-3)
* **Team:** Lovish Chauhan *(Team Leader)* | 14 Members
* **Live Deployment:** `https://road-accident-pattern-analysis.streamlit.app/`

---

### Slide 2: Problem Statement & Engineering Solution
* **The Critical Problem:**
  - Over 150,000 fatal road collisions occur annually across India.
  - Highways suffer from severe winter fog, heavy monsoons, and high vehicle speed differentials.
  - Critical delays in emergency medical assistance during the life-saving "Golden Hour".
* **The Technological Gap:**
  - Traditional safety systems are purely retrospective paper dossiers.
  - Zero real-time integration between roadside weather sensors and physical highway speed signs.
  - Absence of automated dispatch connecting hazard alerts to emergency trauma centers.
* **Our Engineering Solution:**
  - Hybrid Closed-Loop IIoT Platform combining 20,000 real records with live sensing.
  - Empirical Bayesian AI Severity Predictor (Minor, Major, Fatal likelihoods).
  - Dynamic Overhead Variable Message Sign (VMS) speed overrides (80 &rarr; 50 &rarr; 35 km/h).
  - Automated Computer-Aided Dispatch (CAD) to Level-1 trauma centers with 5–8 min ambulance ETAs.

---

### Slide 3: Dataset Grounding (20,000 Real Records Across 8 Corridors)
* **Dataset Attributes & Scope:**
  - **Source:** `indian_roads_dataset.csv` (20,000 empirical accident records × 24 features).
  - **8 Metro Corridors:** Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Pune.
  - **Spatial Features:** Real GPS Coordinates (Lat/Lon), Road Classifications (Highway, Rural, Urban), Lane Counts.
  - **Environmental:** Ambient Weather (Clear, Fog, Rain), Optical Visibility Level, Temperature (°C).
  - **Traffic & Impact:** Traffic Density, Vehicles Involved, Casualties, Severity, Risk Score.
* **Data Pipeline & Cleaning:**
  - Complete Deduplication: Removed duplicate entries and incomplete GPS rows.
  - Noise Elimination: Dropped uninformative columns (e.g. `festival`) to prevent overfitting.
  - Coordinate Normalization: Bounded coordinates strictly to actual metropolitan highway grids.
  - Peak-Hour Extraction: Engineered commuter peak-hour binary flags (08:00–10:00 & 17:00–20:00).
  - Risk Calibration: Normalized composite hazard index into `[0.00, 1.00]` scale.

---

### Slide 4: 3-Tier Industrial IoT (IIoT) System Architecture
* **Tier 1 — Perception Layer (Edge Roadside Sensing):**
  - Optical Visibility Meters, Weather Station, Radar Speed Doppler, Inductive Loop Traffic Counter.
  - Collects continuous telemetry: ambient temperature, optical transmission (fog), precipitation, and speed.
* **Tier 2 — Network & Edge Layer (Inference):**
  - IoT Gateway Node, Rule-Based Hazard Engine, Empirical Bayesian Predictor.
  - Simulates MQTT telemetry streaming. Applies multi-factor hazard checks and computes instant severity likelihoods.
* **Tier 3 — Application & Actuation Layer (Command & Safety):**
  - Streamlit Community Cloud Operator Console, Dynamic VMS Highway Signboard, Emergency CAD Dispatch.
  - Renders live console. Overrides overhead LED speed limits and auto-dispatches Level-1 trauma centers with ETAs.

---

### Slide 5: Module 1 — Historical Accident Analytics Dashboard
* **Multivariate Dynamic Filtering:**
  - Drill down across State, City, Severity, Road Type, and Weather condition in real time.
  - Cascading filters: selecting a state automatically updates available city corridors.
  - Instant recalculation of casualty rates and collision metrics.
* **2×2 Analytical Matrix:**
  - 1. Accidents by Hour of Day: Captures distinct 24h commuting and nighttime peaks.
  - 2. Weather Breakdown: Clear vs. Rain vs. Fog distribution.
  - 3. Severity Split: Minor incidents vs. Major collisions vs. Fatal crashes.
  - 4. Road Infrastructure: High-speed Highways vs. Urban vs. Rural corridors.
* **State Ranking & Data Audit:**
  - Top 10 Indian States aggregated by total accidents and casualty counts.
  - Raw and filtered dataset inspector with one-click CSV export.

---

### Slide 6: AI Feature — Interactive "What-If" Severity Predictor
* **Scenario Simulator Inputs:**
  - Target City Corridor (Bangalore, Delhi, Mumbai, Pune, etc.).
  - Road Classification (Highway, Rural, Urban).
  - Weather Condition (Clear, Fog, Rain) & Optical Visibility (High, Medium, Low).
  - Traffic Density (Low, Medium, High) & 24-Hour Time Slider (0 to 23 Hours).
  - Multi-Vehicle Involvement count (1 to 5 vehicles).
* **Instant Empirical AI Outputs:**
  - **1. Predicted Severity:** Classifies incident as Minor Incident, Major Collision, or Fatal Accident.
  - **2. Probability Distribution:** Exact normalized likelihoods (e.g. Minor: 48% | Major: 36% | Fatal: 16%).
  - **3. Composite Risk Index:** Unified 0.00 to 1.00 score with Low/Moderate/High status.
  - **4. Contributing Hazards:** Flags compounding drivers (e.g. Dense Fog + Night Hours + Multi-Vehicle).
  - **5. Grounded Calibration:** Directly calibrated from empirical Bayes estimates on 20,000 real records.

---

### Slide 7: Module 2 — Roadside Telemetry & Hazard Alert Engine
* **Telemetry Streaming:** Simulated live packet generation from roadside IoT units (5-second auto-refresh option).
* **Multi-Tier Hazard Triage:**
  - **🟢 SAFE / NORMAL:** Clear visibility, dry pavement, normal flow &rarr; Standard speed limits maintained.
  - **🔵 LOW ADVISORY:** Peak-hour commuter congestion on urban roads &rarr; Lane discipline & delay advisories.
  - **🟡 MEDIUM WARNING:** Daytime low visibility, rain, extreme heat (&ge;42°C) &rarr; Advisory speed reduction to 50 km/h.
  - **🔴 HIGH HAZARD:** Dense fog at night, highway rain + heavy traffic, risk &ge; 0.70 &rarr; Mandatory speed override (35 km/h) & CAD ambulance dispatch.

---

### Slide 8: Smart Actuation — Dynamic VMS & Emergency CAD Dispatch
* **💡 Dynamic VMS Highway Signboard:**
  - Closed-Loop Actuation: Real-time physical intervention rather than passive dashboard logging.
  - Overhead Electronic Matrix: Displays glowing condition-specific warnings and speed overrides.
  - Dynamic Speed Limit Dampening: Normal (80 km/h) &rarr; Rain/Traffic (50 km/h) &rarr; Dense Fog/Hazard (Mandatory 35 km/h).
  - Driver Advisories: Prompts "INCREASE HEADWAY", "HAZARD LIGHTS ON", "SLIPPERY ROAD".
* **🚑 Automated CAD Emergency Dispatch:**
  - Computer-Aided Dispatch (CAD): Automates emergency response within the critical "Golden Hour".
  - Regional Level-1 Trauma Hospital Links:
    - *Delhi:* AIIMS Apex Trauma Centre
    - *Mumbai:* KEM Hospital Emergency Unit
    - *Bangalore:* Victoria Hospital Trauma Care
    - *Chandigarh:* PGIMER Level-1 Trauma Wing
  - Real-Time Telematics: Computes assigned ambulance unit ID, highway patrol cruiser, and 5–8 min arrival ETAs.

---

### Slide 9: Team Workload & Contributions by Branch (14 Members)
* **Architecture & Core Modules (Col 1):**
  - **Lovish Chauhan (Lead) [Branch: `Lovish`]:** Live deployment on Streamlit Cloud, What-If Severity Predictor, VMS LED Actuator, CAD dispatch, Windows runner, codebase refactoring.
  - **Krishu Kumar [Branch: `krishu`]:** Created foundational Streamlit dashboard, integrated dataset, authored Colab research notebook, configured Linux packages.
  - **Mayank Gupta [Branch: `mayank`]:** Added core IoT Simulation module (`iot_simulator.py`, `pages/iot_monitor.py`), integrated Pydeck & Numpy requirements.
  - **Alok Chaubey [Branch: `alok`]:** Resolved IoT simulation syntax & deduplication, synchronized state in `streamlit_app.py`, added Dev Container environment.
  - **Arvind Mourya [Branch: `arvind`]:** Implemented State-Wise Accident Analysis module, calculated state grouping aggregations and comparative charts.
* **Features, Analytics & Documentation (Col 2):**
  - **Amit Kohli [Commit: `c8f4245`]:** Engineered Accident Risk & Safety Insights banner with High/Moderate threshold alerts and adverse weather counters.
  - **Ayush Patel [Branch: `ayush`]:** Managed PR #4 integration, synchronized `streamlit_app.py` updates, contributed setup instructions in README.
  - **Pritam Kumar [Branch: `pritam`]:** Enhanced `iot_simulator.py` sensor generator and refined IoT monitor UI alert cards and multi-page routing.
  - **Kritika [Branch: `kritikaaa`]:** Authored `CONTRIBUTING.md` setup guide, validated IoT simulation telemetry parameters.
  - **Sunal, Daniyal, Riddhi, Ayan, Om:** Sunal (parameter updates), Daniyal (notebook standardization), Riddhi (accident research), Ayan (PR #3 merge), Om (QA review).

---

### Slide 10: Empirical Results, Real-World Impact & Conclusion
* **Empirical Hazard Findings:**
  - Dense winter fog + night hours (21:00–05:00) causes a **+42% spike in fatal collisions**.
  - Highways account for **2.3× higher casualty rates per crash** compared to urban roads, validating the need for dynamic VMS speed dampening.
* **Intelligent Safety Impact:**
  - Dynamic VMS speed intervention (reducing limits to 35–40 km/h) dampens vehicle approach momentum before blackspots.
  - Automated CAD dispatch routes Level-1 trauma centers with **5–8 min ambulance ETAs**, cutting response lag within the critical "Golden Hour".
* **Project Status & Roadmap:**
  - **✓ Production Ready:** 100% deployed live on Streamlit Community Cloud ([https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/)).
  - **✓ Unified Architecture:** Single-entrypoint architecture on `streamlit_app.py`.
  - **Future Roadmap:** Physical ESP32 LoRaWAN hardware flashing and YOLOv8 CCTV crash detection.
