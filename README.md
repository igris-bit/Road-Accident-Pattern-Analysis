# Road Accident Pattern Analysis

Analyze de-identified accident records to describe patterns by time, road type, weather, or severity.

---

## 📌 Project Overview
 
A multi-page **Streamlit** web dashboard built on the **Indian Roads Dataset** (20,000 accident records across Indian cities). The project has two modules:

### Module 1 — Accident Pattern Analysis Dashboard (`streamlit_app.py`)
Interactive analysis of historical accident data with:
- Filters: State, City, Severity, Weather, Road Type
- Charts: Accidents by Hour, Weather, Severity, Road Type
- Metrics: Total Accidents, Casualties, Fatal %, Average Risk Score
- State-wise Analysis: Top 10 States by accident volume and casualties
- **What-If Risk & Severity Predictor**: Interactive scenario simulator predicting accident severity probabilities (Minor, Major, Fatal) and key hazard contributors
- Summary tables & raw data download

### Module 2 — IIoT Simulation & Smart Highway Actuation (`pages/iot_monitor.py`)
Real-time roadside sensor simulation and industrial actuation across 8 Indian corridors:
- **Live Sensor Feed** — roadside optical, weather, and traffic density telemetry
- **Rule-Based Alert Engine** — flags HIGH / MEDIUM / LOW / SAFE hazard conditions
- **Smart Highway VMS Actuator** — overhead electronic LED Variable Message Sign with dynamic speed limit overrides and hazard warnings
- **Automated Emergency CAD Dispatch** — simulated hospital trauma centre routing, ambulance unit ETA, and highway patrol dispatch
- **Risk Score Gauge** — visual 0.0–1.0 corridor danger index
- **Accident Hotspot Map** — interactive pydeck geospatial map of real accidents and live sensor node
- **Historical Context Panel** — real dataset statistics for the selected metropolitan corridor
- **Incident Audit Log** — session-based alert history with CSV export

---

## 🗂️ Project Organization & File Structure

```
Road-Accident-Pattern-Analysis/
│
├── .vscode/                               # Workspace configuration
│   └── settings.json                      # Python 3.12 interpreter path
│
├── docs/                                  # Official Submission Materials
│   ├── SUBMISSION_DETAILS.md              # All 4 mandatory submission links & checklist
│   ├── TEAM_CONTRIBUTIONS.md              # Honest 14-member contribution & evaluation matrix
│   ├── PROJECT_REPORT.md                  # Comprehensive IEEE-style project report
│   └── presentation/                      # Presentation deck
│       └── PROJECT_PPT_OUTLINE.md         # 12-slide presentation structure & speaking notes
│
├── notebooks/                             # Research & Exploratory Data Analysis
│   └── Road_Accident_Pattern_Analysis.ipynb # Colab / Jupyter analysis notebook
│
├── pages/                                 # Multi-Page Streamlit Navigation
│   └── iot_monitor.py                     # Module 2: IIoT Telemetry, VMS & CAD Dispatch
│
├── indian_roads_dataset.csv               # Ground-truth dataset (20,000 records × 24 features)
├── iot_simulator.py                       # IIoT simulation & predictive severity engine
├── streamlit_app.py                       # Module 1: Main Dashboard entry point (Streamlit Cloud)
├── requirements.txt                       # Python dependencies
├── packages.txt                           # System-level dependencies
└── run_app.bat                            # One-click Windows application launcher
```

---

## ⚙️ Setup & Run

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Navigate to **IoT Monitor** in the sidebar for the simulation module.

---

## 📦 Dependencies

```
streamlit · pandas · matplotlib · seaborn · numpy · pydeck
```
