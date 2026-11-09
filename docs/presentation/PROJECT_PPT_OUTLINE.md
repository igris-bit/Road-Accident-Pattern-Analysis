# 🖥️ Project Presentation (PPT) — Modern 10-Slide Deck Outline

**Project Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring  
**Course:** Industrial Internet of Things (IIoT-3)  
**Team Leader:** Lovish Chauhan (`lovishneeraj@gmail.com`)  
**Team Size:** 14 Members  
**Design Theme:** Fresh Modern "Clean Tech" (Slate-50 Canvas, Crisp White Card Panels, Royal Blue & Emerald Accents, High-Legibility Typography)  
**🌐 Live Web App:** [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/)  
**GitHub Repository:** [https://github.com/igris-bit/Road-Accident-Pattern-Analysis](https://github.com/igris-bit/Road-Accident-Pattern-Analysis)  

---

### Slide 1: Title & Hero Slide (Clean Tech Executive)
* **Pill Badge:** `ACADEMIC CAPSTONE PROJECT | IIoT-3 SMART MOBILITY`
* **Title:** Road Accident Pattern Analysis & IIoT Smart Highway Monitoring
* **Subtitle:** Closed-Loop Intelligent Transportation System (ITS) • Empirical AI Severity Prediction • Dynamic VMS Actuation
* **Leadership Card:** Lovish Chauhan *(Team Leader)* | 14 Active Contributors
* **Live Deployment Card:** Streamlit Cloud — `road-accident-pattern-analysis.streamlit.app`
* **Repository Card:** GitHub — `igris-bit/Road-Accident-Pattern-Analysis`

---

### Slide 2: The Road Safety Crisis & Our IIoT Solution (3 Cards)
* **Card 1: The Critical Crisis (150,000+ Deaths / Yr):**
  - **36% Fatalities on Highways:** National highways account for 36% of all traffic deaths despite being <2% of total road network.
  - **Adverse Weather Multipliers:** Dense winter fog, monsoon hydroplaning, and night-time speed differentials trigger catastrophic multi-vehicle pileups.
  - **Delayed Golden Hour:** Critical collision victims suffer fatal medical delays due to absence of automated emergency dispatch.
* **Card 2: The Technology Gap (100% Retrospective):**
  - **Post-Incident Audits:** Legacy highway management relies strictly on retrospective police FIRs and delayed annual paperwork.
  - **Zero Edge Actuation:** Roadside weather and visibility sensors do not communicate with overhead speed limit signs in real time.
  - **Manual Emergency Calls:** Ambulance dispatch depends entirely on manual phone calls from injured or panicked motorists.
* **Card 3: Our Engineering Solution (Closed-Loop ITS):**
  - **20,000 Empirical Records:** Calibrated on verified Indian road accident records across 8 major metropolitan corridors.
  - **Real-Time AI Severity Model:** Computes instant Minor, Major, and Fatal probabilities plus composite risk scoring.
  - **Dynamic VMS & CAD Dispatch:** Overrides overhead LED speed limits (80 &rarr; 50 &rarr; 35 km/h) and alerts Level-1 trauma centers.

---

### Slide 3: Dataset Grounding (20,000 Records Across 8 Corridors)
* **Top Metric Callouts:**
  - `20,000` Verified Accident Incidents (Royal Blue)
  - `8 Metros` Major Indian City Corridors (Emerald Green)
  - `24 Attributes` Spatial, Weather & Traffic Fields (Purple)
* **Panel 1 — Scope & Spatial Grounding:**
  - **Primary Data File:** `indian_roads_dataset.csv` containing 20,000 verified rows × 24 columns.
  - **8 Metropolitan Hubs:** Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Pune.
  - **Spatial Dimensions:** Real GPS Lat/Lon coordinates, Road Types (Highway, Rural, Urban), and Lane counts.
  - **Environmental Attributes:** Clear, Dense Fog, Heavy Rain | Visibility indices | Road surface wetness.
* **Panel 2 — Data Engineering Pipeline:**
  - **Deduplication & Null Handling:** Identified and removed duplicate rows & incomplete GPS coordinate records.
  - **Noise Elimination:** Pruned uninformative columns (e.g. `festival`) to avoid model distortion.
  - **Coordinate Normalization:** Bounded coordinates strictly to regional metropolitan belts across India.
  - **Feature Engineering:** Extracted rush-hour commuting flags (08:00–10:00 & 17:00–20:00) for risk modeling.

---

### Slide 4: 3-Tier IIoT System Architecture
* **Tier 1: Perception Layer (Roadside Sensor Telemetry):**
  - **Sensors:** Optical Visibility Meters • Roadside Weather Station • Radar Speed Doppler • Traffic Inductive Loops
  - **Technical Role:** Continuous highway telemetry capture — ambient temperature, optical transmission (fog), precipitation, and vehicle speed.
* **Tier 2: Network & Edge Layer (IoT Gateway & Inference):**
  - **Components:** IoT Gateway Node • Multi-Factor Hazard Escalation Engine • Empirical Bayesian Severity Predictor
  - **Technical Role:** Ingests telemetry packets via simulated MQTT/REST. Evaluates multi-factor hazard rules & computes instant severity likelihoods.
* **Tier 3: Application & Actuation Layer (Command & Control):**
  - **Actuators:** Streamlit Cloud Dashboard • Dynamic Overhead VMS Signs • Automated CAD Emergency Dispatch
  - **Technical Role:** Overrides physical overhead LED speed limits (80 &rarr; 50 &rarr; 35 km/h) & auto-dispatches Level-1 trauma centers with ETAs.

---

### Slide 5: Module 1 — Historical Accident Analytics Dashboard
* **Card 1: Dynamic Multi-Filter Slicers:**
  - **State & Municipal Cascading:** Selecting a state automatically narrows down available municipal corridors in real time.
  - **Real-Time KPI Recalculation:** Instantly recalculates total casualty toll, collision counts, and corridor risk metrics.
  - **Infrastructure & Weather Filters:** Drill down across Highway/Urban and Clear/Rain/Fog scenarios simultaneously.
* **Card 2: 2×2 Core Analytical Matrix:**
  - **Accidents by Hour:** Pinpoints 24h commuting spikes (08–10h & 17–20h) and dangerous late-night surges (22–03h).
  - **Weather Collision Impact:** Quantifies distribution between Clear, Rain, and Dense Fog collision clusters.
  - **Severity Stratification:** Visualizes proportion of Minor Incidents vs. Major Collisions vs. Fatal Crashes.
  - **Road Classification:** Contrasts high-speed highway casualty rates against urban and rural corridors.
* **Card 3: State Rankings & Data Audit:**
  - **Top 10 Indian States:** Ranks states by collision frequency, casualty count, and fatality ratio.
  - **Raw Data Inspection:** Embedded dataset viewer with dynamic column sorting and real-time search.
  - **One-Click CSV Export:** Enables municipal traffic police and safety engineers to download filtered audits.

---

### Slide 6: AI Predictive Feature — Interactive "What-If" Severity Predictor
* **Left Panel — Adjustable Simulation Inputs:**
  - **Corridor Metropolitan City:** Choose from Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai, Pune.
  - **Road Classification:** High-Speed Highway, Rural Arterial, or Urban City Road.
  - **Weather & Visibility:** Clear, Dense Fog, Heavy Rain | High, Moderate, or Low Optical Visibility.
  - **Traffic Density & Commute Hour:** Low, Medium, High Density | 24-Hour Slider (0 to 23 Hours).
  - **Vehicular Impact Count:** Number of vehicles involved in the collision scenario (1 to 5 vehicles).
* **Right Panel — Real-Time Empirical AI Outputs:**
  - **Predicted Severity Category:** Immediate classification into Minor Incident, Major Collision, or Fatal Crash.
  - **Probability Distribution (%):** Exact empirical likelihoods (e.g. Minor: 48% | Major: 36% | Fatal: 16%).
  - **Composite Risk Index:** Unified 0.00 to 1.00 risk score with Low / Moderate / High status indicator.
  - **Compounding Factor Analysis:** Automatically flags hazard combinations (e.g. Dense Fog + Night Hours + Multi-Vehicle).
  - **Empirical Grounding:** Directly computed from Laplace-smoothed Bayes probabilities on 20,000 real records.

---

### Slide 7: Module 2 — Live Telemetry, Smart VMS Signs & Emergency CAD
* **Card 1: 4-Tier Hazard Alert Engine:**
  - **🟢 SAFE STATUS:** Optimal visibility & dry road &rarr; Standard speed limits (80 km/h).
  - **🔵 LOW STATUS:** Peak-hour urban congestion &rarr; Advisory lane discipline warnings.
  - **🟡 MEDIUM STATUS:** Low visibility, rain, or heat &ge;42°C &rarr; Advisory speed cut to 50 km/h.
  - **🔴 HIGH HAZARD:** Dense night fog, highway rain, risk &ge;0.70 &rarr; Mandatory 35 km/h override & CAD dispatch.
* **Card 2: 💡 Dynamic Variable Message Sign (VMS):**
  - **Closed-Loop Physical Actuation:** Moves beyond passive dashboards to real-time roadside safety intervention.
  - **Overhead LED Matrix:** Renders amber/red LED matrix typography overriding highway speed limits in real time.
  - **Dynamic Speed Dampening:** Automatically forces speed reduction (80 &rarr; 50 &rarr; 35 km/h) ahead of blackspots.
  - **Active Driver Advisories:** Flashes "DENSE FOG DETECTED", "KEEP SAFE HEADWAY", "HAZARD LIGHTS ON".
* **Card 3: 🚑 Automated Emergency CAD Dispatch:**
  - **Rapid Golden Hour Response:** Drastically cuts emergency delay for critical trauma collision victims.
  - **Regional Trauma Center Routing:** Direct routing to AIIMS (Delhi), KEM (Mumbai), Victoria (Bangalore), PGIMER (Chandigarh).
  - **Real-Time Telematics Dispatch:** Assigns ambulance unit ID, highway patrol cruiser, distance (km), and 5–8 min arrival ETAs.

---

### Slide 8: Team Member Contributions by Branch (Part 1 — Members 1 to 7)
* **Left Container: Architecture, Cloud Deployment & Simulation:**
  - **Lovish Chauhan [Branch: `Lovish`]:** Team Leader. Architected end-to-end ITS system; built What-If Severity Predictor, dynamic VMS actuator, and CAD dispatch in `streamlit_app.py`; managed Streamlit Cloud deployment; authored `run_app.bat` runner.
  - **Krishu Kumar [Branch: `krishu`]:** Core Developer. Developed foundational Streamlit dashboard (`fca04dc`), integrated 20,000-row Indian accident dataset, authored Google Colab research notebook (`98f279f`), configured Linux `packages.txt`.
  - **Mayank Gupta [Branch: `mayank`]:** IoT Specialist. Authored core IIoT simulation module (`iot_simulator.py`, `pages/iot_monitor.py`); integrated Pydeck geospatial layers and real-time sensor generation pipelines.
  - **Alok Chaubey [Branch: `alok`]:** Full Stack Dev. Resolved IoT syntax errors and deduplicated sensor methods (`5f14dde`); synchronized state variables in `streamlit_app.py`; created Dev Container configuration (`e5dfaf4`).
* **Right Container: Analytics Modules, Risk Logic & PR Sync:**
  - **Arvind Mourya [Branch: `arvind`]:** Data Analyst. Engineered State-Wise Accident Analysis dashboard (`567d35e`); computed Top 10 state grouping aggregations, casualty totals, and interactive Plotly comparative charts.
  - **Amit Kohli [Commit: `c8f4245`]:** Feature Engineer. Engineered Accident Risk & Safety Insights banner with High/Moderate threshold alerts and adverse weather frequency counters.
  - **Ayush Patel [Branch: `ayush`]:** Integration Engineer. Managed PR #4 integration (`c108d2c`); synchronized `streamlit_app.py` updates; authored setup and dependency installation documentation in `README.md`.

---

### Slide 9: Team Member Contributions by Branch (Part 2 — Members 8 to 14)
* **Left Container: UI Telemetry, Guidelines & Schema Audit:**
  - **Pritam Kumar (Athox-X) [Branch: `pritam`]:** UI Developer. Enhanced `iot_simulator.py` sensor generation logic (`0aa5a8d`) and customized alert banner CSS styling in `pages/iot_monitor.py` (`03be2bc`).
  - **Kritika [Branch: `kritikaaa`]:** Documentation. Authored `CONTRIBUTING.md` team setup instructions (`17c34b4`), verified simulation parameter boundaries, and assisted in documentation.
  - **Sunal [Branch: `sunal`]:** IoT Tester. Updated `iot_monitor.py` parameters (`b54a36b`), authored multiple `README.md` documentation revisions (`f81277d`, `82a8fdd`).
  - **Daniyal Malik [Branch: `Daniyal`]:** Notebook QA. Standardized notebook naming to `Road_Accident_Pattern_Analysis.ipynb` (`3758353`) and verified dataset column schemas.
* **Right Container: Research, PR Verification & Cross-Testing:**
  - **Riddhi Gupta [Branch: `Riddhi-Gupta`]:** Research Analyst. Documented project feature overviews in `README.md` (`91db893`), researched Indian metropolitan accident statistics and corridor parameters.
  - **Ayan Ansari [Branch: `ayan`]:** Release Engineer. Managed PR #3 merge from Krishu (`434d47e`), updated deployment notes in `README.md` (`d6668d4`), and conducted branch validation.
  - **Om [Branch: `om`]:** QA & Reviewer. Participated in peer code review cycles, tested sidebar filter widgets, and validated UI responsiveness across desktop and mobile screens.

---

### Slide 10: Empirical Findings, Real-World Impact & Submission Deliverables
* **Card 1: Key Empirical Findings:**
  - **+42% Fatal Fog Surge:** Dense winter fog combined with night hours (21:00–05:00) causes a +42% spike in fatal collisions.
  - **2.3× Highway Fatality Rate:** High-speed national highways produce 2.3x higher casualty rates per collision compared to urban streets.
  - **Speed Differential Hazard:** Variance between freight haulers and commuter vehicles triggers deadly rear-end impacts.
* **Card 2: Intelligent Safety Impact:**
  - **Proactive Prevention:** Dynamic VMS speed dampening forces safe approach speeds ahead of high-risk accident blackspots.
  - **Golden Hour Trauma Care:** Automated CAD dispatch eliminates manual emergency delays, routing trauma ambulances in 5–8 mins.
  - **Closed-Loop Safety Model:** Shifts national highway management from reactive police FIRs to active real-time incident prevention.
* **Card 3: Official Project Deliverables (Submission Links):**
  - 🌐 **Live Web Application:** [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/)
  - 💻 **GitHub Repository:** [https://github.com/igris-bit/Road-Accident-Pattern-Analysis](https://github.com/igris-bit/Road-Accident-Pattern-Analysis)
  - 📄 **IEEE Project Report:** Complete academic PDF report in `docs/report/Road_Accident_Pattern_Analysis_Project_Report.pdf`
  - 📊 **Presentation Deck:** Full 10-slide executive presentation in `docs/presentation/Road_Accident_Pattern_Analysis_Presentation.pptx`
