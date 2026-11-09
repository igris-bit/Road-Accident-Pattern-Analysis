# Road Accident Pattern Analysis

Analyze de-identified accident records to describe patterns by time, road type, weather, or severity.

---

## 📌 Project Overview
 
A multi-page **Streamlit** web dashboard built on the **Indian Roads Dataset** (20,000 accident records across Indian cities). The project has two modules:

### Module 1 — Accident Pattern Analysis Dashboard (`app.py`)
Interactive analysis of historical accident data with:
- Filters: State, City, Severity, Weather, Road Type
- Charts: Accidents by Hour, Weather, Severity, Road Type
- Metrics: Total Accidents, Casualties, Fatal %, Average Risk Score
- Summary tables & raw data download

### Module 2 — IoT Simulation & Alert Monitoring (`pages/iot_monitor.py`)
Real-time roadside sensor simulation with hazard alert detection:
- **Live Sensor Feed** — generates realistic IoT readings (weather, visibility, temperature, traffic density, risk score)
- **Rule-Based Alert Engine** — flags HIGH / MEDIUM / LOW / SAFE conditions using the same data fields as the real dataset
- **Risk Score Gauge** — visual 0.0–1.0 indicator colour-coded by danger level
- **Accident Hotspot Map** — interactive pydeck map of real accident locations (lat/lon) from the dataset
- **Historical Context Panel** — shows real dataset statistics for the simulated sensor's city
- **Alert History Log** — session-based log of all alerts with CSV download

---

## 🗂️ File Structure

```
├── app.py                              # Main dashboard (Module 1)
├── streamlit_app.py                    # Alias of app.py
├── iot_simulator.py                    # IoT engine: sensor generator + alert rules (Module 2)
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
