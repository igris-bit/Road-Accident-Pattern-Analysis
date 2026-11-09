# Road Accident Pattern Analysis

Analyze de-identified accident records to describe patterns by time, road type, weather, or severity.

---

## 📌 Project Overview
 
A multi-page **Streamlit** web dashboard built on the **Indian Roads Dataset** (20,000 accident records across Indian cities). The project has two modules:

### Module 1 — Accident Pattern Analysis Dashboard (`streamlit_app.py` / `app.py`)
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

## 🗂️ File Structure

```
├── app.py                              # Main dashboard (Module 1)
├── streamlit_app.py                    # Alias of app.py
├── iot_simulator.py.                   # IoT engine: sensor generator + alert rules (Module 2)
├── pages/
│   └── iot_monitor.py                  # IoT Streamlit page (Module 2)
├── indian_roads_dataset.csv            # Dataset: 20,000 rows × 24 columns
├── Road_Accident_Pattern_Analysis.ipynb # EDA notebook (Google Colab)
├── requirements.txt                    # Python dependencies
└── packages.txt                        # System packages
```

---

## ⚙️ Setup & Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Navigate to **IoT Monitor** in the sidebar for the simulation module.

---

## 📦 Dependencies

```
streamlit · pandas · matplotlib · seaborn · numpy · pydeck
```
