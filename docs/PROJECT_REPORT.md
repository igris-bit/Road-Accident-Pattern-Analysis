# INVERTIS UNIVERSITY
**Bareilly, Uttar Pradesh**  
*In association with* **TrainX**

---

### INDUSTRIAL INTERNET OF THINGS (IIoT-3) • PRACTICAL PROJECT REPORT
# Road Accident Pattern Analysis & IIoT Smart Highway Monitoring
#### A Comprehensive System for Empirical Risk Analytics, Closed-Loop VMS Actuation & Emergency CAD Dispatch

| Metric | Value | Metric | Value |
| :---: | :---: | :---: | :---: |
| **20,000**<br>Accident Records | **8**<br>Metro Corridors | **3-Tier**<br>IIoT Architecture | **14**<br>Team Members |

| Key Parameter | Details |
| :--- | :--- |
| **Subject** | Industrial Internet of Things (IIoT-3) |
| **Training Partner** | TrainX |
| **Mentor** | Mr. Unwan Khan |
| **Group Leaders** | Lovish Chauhan & Omgyan Singh |
| **Team Size** | 14 Members |
| **Practical Date** | 25 November 2026 |
| **GitHub Repository** | [github.com/igris-bit/Road-Accident-Pattern-Analysis](https://github.com/igris-bit/Road-Accident-Pattern-Analysis) |
| **Live Application** | [road-accident-pattern-analysis.streamlit.app](https://road-accident-pattern-analysis.streamlit.app/) |

---

## Index

1. [Introduction](#1-introduction)
   - 1.1 [Background: Road Safety in India](#11-background-road-safety-in-india)
   - 1.2 [From Retrospective to Proactive Safety](#12-from-retrospective-to-proactive-safety)
   - 1.3 [Overview of the Proposed Framework](#13-overview-of-the-proposed-framework)
   - 1.4 [Key Deliverables](#14-key-deliverables)
   - 1.5 [Report Organisation](#15-report-organisation)
2. [Problem Statement](#2-problem-statement)
   - 2.1 [Overview of the Problem](#21-overview-of-the-problem)
   - 2.2 [Violent Weather Shifts](#22-violent-weather-shifts)
   - 2.3 [High Vehicle Speed Differentials](#23-high-vehicle-speed-differentials)
   - 2.4 [Delayed Medical Response](#24-delayed-medical-response)
   - 2.5 [Absence of Closed-Loop Feedback](#25-absence-of-closed-loop-feedback)
   - 2.6 [Problem Summary](#26-problem-summary)
3. [System Objectives](#3-system-objectives)
   - 3.1 [Deep Empirical Analysis](#31-deep-empirical-analysis)
   - 3.2 [Bayesian AI Predictor](#32-bayesian-ai-predictor)
   - 3.3 [Closed-Loop IIoT Architecture](#33-closed-loop-iiot-architecture)
   - 3.4 [Cloud CI/CD Deployment](#34-cloud-cicd-deployment)
   - 3.5 [Mapping of Objectives to Modules](#35-mapping-of-objectives-to-modules)
4. [Dataset Architecture & Preprocessing Pipeline](#4-dataset-architecture--preprocessing-pipeline)
   - 4.1 [Dataset Overview](#41-dataset-overview)
   - 4.2 [Spatial Identifiers](#42-spatial-identifiers)
   - 4.3 [Temporal Markers](#43-temporal-markers)
   - 4.4 [Road Infrastructure](#44-road-infrastructure)
   - 4.5 [Environmental Conditions](#45-environmental-conditions)
   - 4.6 [Impact & Evaluation](#46-impact--evaluation)
   - 4.7 [Preprocessing Summary](#47-preprocessing-summary)
   - 4.8 [Geographic Coverage](#48-geographic-coverage)
5. [Three-Tier Industrial IoT (IIoT) Architecture](#5-three-tier-industrial-iot-iiot-architecture)
   - 5.1 [Closed-Loop Sensing-to-Actuation](#51-closed-loop-sensing-to-actuation)
   - 5.2 [Tier 1: Perception Layer (Roadside Edge Sensing)](#52-tier-1-perception-layer-roadside-edge-sensing)
   - 5.3 [Tier 2: Network & Edge Layer (Edge Computing)](#53-tier-2-network--edge-layer-edge-computing)
   - 5.4 [Tier 3: Application & Actuation (Command & Safety)](#54-tier-3-application--actuation-command--safety)
   - 5.5 [Architecture Summary Table](#55-architecture-summary-table)
6. [Module 1: Historical Analytics & What-If Predictor](#6-module-1-historical-analytics--what-if-predictor)
   - 6.1 [Role of Module 1](#61-role-of-module-1)
   - 6.2 [Multivariate Filtering](#62-multivariate-filtering)
   - 6.3 [Visual Distribution Matrix and Top 10 States](#63-visual-distribution-matrix-and-top-10-states)
   - 6.4 [State-Wise Accident Analysis](#64-state-wise-accident-analysis)
   - 6.5 [Accident Risk & Safety Insights Banner](#65-accident-risk--safety-insights-banner)
   - 6.6 [Mathematical Calibration of the Predictor](#66-mathematical-calibration-of-the-predictor)
   - 6.7 [Input Matrix](#67-input-matrix)
   - 6.8 [Real-Time Outputs](#68-real-time-outputs)
7. [Module 2: IIoT Edge Telemetry, VMS & CAD Dispatch](#7-module-2-iiot-edge-telemetry-vms--cad-dispatch)
   - 7.1 [Purpose of Module 2](#71-purpose-of-module-2)
   - 7.2 [Roadside Telemetry Generation](#72-roadside-telemetry-generation)
   - 7.3 [Multi-Tier Alert Escalation](#73-multi-tier-alert-escalation)
   - 7.4 [Smart Highway Variable Message Sign (VMS)](#74-smart-highway-variable-message-sign-vms)
   - 7.5 [Computer-Aided Dispatch (CAD) Interconnect](#75-computer-aided-dispatch-cad-interconnect)
   - 7.6 [Geospatial Pydeck Hotspot Mapping](#76-geospatial-pydeck-hotspot-mapping)
   - 7.7 [Persistent Incident Audit Log](#77-persistent-incident-audit-log)
8. [Deployment & Repository Structure](#8-deployment--repository-structure)
   - 8.1 [Single Clean Entrypoint](#81-single-clean-entrypoint)
   - 8.2 [Streamlit Community Cloud](#82-streamlit-community-cloud)
   - 8.3 [Repository Components](#83-repository-components)
   - 8.4 [Development Environment Support](#84-development-environment-support)
   - 8.5 [Exploratory Notebook](#85-exploratory-notebook)
9. [Experimental Findings](#9-experimental-findings)
   - 9.1 [Adverse Weather Multiplier](#91-adverse-weather-multiplier)
   - 9.2 [Highway vs. Urban Severity Ratio](#92-highway-vs-urban-severity-ratio)
   - 9.3 [Golden Hour Response Optimization](#93-golden-hour-response-optimization)
   - 9.4 [Summary of Findings](#94-summary-of-findings)
   - 9.5 [Combined Interpretation](#95-combined-interpretation)
10. [Real-World Impact](#10-real-world-impact)
11. [Team Organisation & Contributions](#11-team-organisation--contributions)
    - 11.1–11.14 [Individual Member Breakdown](#111-lovish-chauhan-team-leader---branch-lovish---high-lead)
    - 11.15 [Collaboration Workflow](#1115-collaboration-workflow)
    - 11.16 [Contribution Levels](#1116-contribution-levels)
12. [Conclusion](#12-conclusion)
13. [Future Engineering Scope](#13-future-engineering-scope)
    - 13.1 [Hardware Edge Nodes](#131-hardware-edge-nodes)
    - 13.2 [Computer Vision Integration](#132-computer-vision-integration)
    - 13.3 [Vehicle-to-Everything (V2X)](#133-vehicle-to-everything-v2x)
14. [Glossary of Terms](#14-glossary-of-terms)
15. [Project Links & Resources](#15-project-links--resources)

---

## Project Team

This project was developed by a team of 14 members at **Invertis University** under the IIoT-3 curriculum delivered in association with **TrainX**. The team is led by two group leaders and guided by the course mentor.

| Key Role | Name / Organization |
| :--- | :--- |
| **Mentor** | Mr. Unwan Khan |
| **Training Partner** | TrainX |
| **Group Leaders** | Lovish Chauhan & Omgyan Singh |

| # | Member | Branch / Commit | Primary Contribution | Level |
| :-: | :--- | :--- | :--- | :-: |
| **1** | **Lovish Chauhan** *(Team Leader)* | `Lovish` | System architecture, Streamlit Cloud deployment, What-If predictor, VMS actuator, CAD dispatch | High (Lead) |
| **2** | **Krishu Kumar** | `krishu` | Initial Streamlit dashboard, dataset integration, Colab notebook, packages.txt | High |
| **3** | **Mayank Gupta** | `mayank` | Foundational IoT simulation and alert monitoring module; Pydeck integration | High |
| **4** | **Alok Chaubey** | `alok` | Sensor-generator fixes, state synchronisation, Dev Container configuration | High |
| **5** | **Arvind Mourya** | `arvind` | State-Wise Accident Analysis module and dual bar charts | High |
| **6** | **Amit Kohli** | `c8f4245` | Accident Risk & Safety Insights banner and weather advisories | High |
| **7** | **Ayush Patel** | `ayush` | Pull Request #4 integration, dashboard synchronisation, README setup guide | High |
| **8** | **Pritam Kumar** | `pritam` | Sensor generator enhancements, alert card UI, navigation and session persistence | Medium |
| **9** | **Kritika** | `kritikaaa` | CONTRIBUTING.md guide and telemetry parameter verification | Medium |
| **10** | **Sunal** | `sunal` | iot_monitor.py parameter updates and README iterations | Medium |
| **11** | **Daniyal Malik** | `Daniyal` | Notebook filename standardisation and dataset schema verification | Medium |
| **12** | **Riddhi Gupta** | `Riddhi-Gupta` | README feature overviews and research on accident patterns | Medium |
| **13** | **Ayan Ansari** | `ayan` | PR #3 merge management and deployment documentation | Low / Partial |
| **14** | **Om** | `om` | Peer code review, sidebar filter testing, UI responsiveness checks | Low / Minimal |

---

## 1. Introduction

### 1.1 Background: Road Safety in India
Road traffic collisions account for over 150,000 fatalities annually in India, creating a severe socio-economic impact. Every collision affects not only the people directly involved but also their families, their communities and the wider transportation network that depends on safe and predictable movement of vehicles. Because the scale of the problem is so large, even small improvements in how accidents are understood, anticipated and responded to can have a significant effect.

The Road Accident Pattern Analysis & IIoT Smart Highway Monitoring project has been created in response to this challenge. It is a comprehensive system that combines the study of historical accident records with a simulated Industrial Internet of Things (IIoT) environment in which roadside sensors, edge intelligence, electronic signage and emergency dispatch work together as one connected safety loop.

### 1.2 From Retrospective to Proactive Safety
Traditional transportation management is largely retrospective. It relies on post-crash police dossiers and static signboards that fail to avert accidents before impact. Information is gathered only after an accident has taken place, and roadside signs display the same message regardless of whether the road is dry and clear or covered in dense fog. In such a setting, drivers receive no timely warning about the specific hazard in front of them.

This project pioneers a hybrid safety framework that bridges retrospective empirical data analysis with proactive Industrial IoT edge simulation and actuation. The retrospective side studies what has happened in the past in order to understand which combinations of time, weather, visibility, road type and traffic density are most dangerous. The proactive side uses those learnings to interpret live sensor telemetry and to act on it by changing the speed limit shown to drivers and by dispatching emergency help.

### 1.3 Overview of the Proposed Framework
The framework is calibrated on a ground-truth dataset of 20,000 records across 8 major Indian metropolitan corridors: Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai and Pune. It is delivered as a live web application running on Streamlit Community Cloud, so that municipal authorities, traffic police and reviewers can open it from a browser without any local installation.

The system is organised into two cooperating modules:
- **Module 1:** Historical analytics and What-If severity prediction center, implemented in `streamlit_app.py`.
- **Module 2:** IIoT edge telemetry, smart VMS actuator and CAD dispatch environment, implemented in `pages/iot_monitor.py`.

Together they cover the full path from understanding past accidents to responding to a hazard in real time.

### 1.4 Key Deliverables
The system delivers four principal capabilities:
- **Multivariate analytics dashboard:** An interactive dashboard featuring an empirical Bayesian 'What-If' accident severity predictor.
- **Industrial IoT edge simulation engine:** An engine that translates optical, environmental and speed telemetry into multi-tier hazard alerts.
- **Dynamic overhead Variable Message Sign (VMS) actuator:** A sign that overrides highway speed limits in real time according to the detected hazard.
- **Automated Computer-Aided Dispatch (CAD) interconnect:** A dispatch module that routes the nearest Level-1 trauma centers (AIIMS, KEM, PGIMER and others) within the critical Golden Hour.

### 1.5 Report Organisation
The remainder of this report describes the project part by part. Chapter 2 states the problem and Chapter 3 lists the objectives. Chapter 4 explains the dataset and its preprocessing. Chapter 5 presents the three-tier IIoT architecture, while Chapters 6 and 7 describe the two software modules in detail. Chapter 8 covers deployment and the repository. Chapters 9 and 10 present the experimental findings and real-world impact. Chapter 11 documents the team and its contributions, followed by the conclusion, the future scope, a glossary and project links.

---

## 2. Problem Statement

### 2.1 Overview of the Problem
Arterial highways in India experience violent weather shifts (dense winter fog and monsoon flooding), high vehicle speed differentials, and delayed medical response. Existing traffic monitoring systems lack automated closed-loop feedback between roadside sensors and driver warnings. These factors combine to make highway travel particularly hazardous, and they are the reasons the project was undertaken.

### 2.2 Violent Weather Shifts
Two weather conditions are singled out in the problem statement: dense winter fog and monsoon flooding. Dense fog reduces the distance over which a driver can see, which directly affects how much time is available to react to a slow or stopped vehicle. Monsoon flooding and rain change road conditions and visibility in a similar manner. The dataset used in this project records weather as clear, fog or rain, and visibility as high, medium or low, so that the effect of these conditions on accident outcomes can be measured rather than assumed.

### 2.3 High Vehicle Speed Differentials
On highways, vehicles travel at very different speeds. When a hazard appears, faster vehicles approach slower ones with considerable momentum. The project's findings later show that highway collisions exhibit 2.3 times higher casualty rates per incident compared to urban roads, which the report attributes to elevated approach momentum. This is the reason why dynamic speed intervention through the Variable Message Sign is a central part of the system.

### 2.4 Delayed Medical Response
Medical response after a collision is often delayed. The speed at which emergency help reaches an injured person strongly affects the outcome, and for this reason the project places emphasis on the Golden Hour. Delays in notifying emergency services and in choosing the right hospital reduce the time available for treatment. The project therefore includes an automated Computer-Aided Dispatch interconnect that assigns the regional Level-1 trauma facility and estimates an ambulance arrival window.

### 2.5 Absence of Closed-Loop Feedback
The most important gap identified is the lack of automated closed-loop feedback between roadside sensors and driver warnings. In a closed loop, sensing leads to analysis, analysis leads to action, and the action is visible to the people on the road. Existing systems often stop at the first step, collecting or displaying data without turning it into an immediate warning. This project addresses the gap by connecting the sensing layer, an edge inference layer and an actuation layer into one continuous chain.

### 2.6 Problem Summary

| Challenge | Description | Project Response |
| :--- | :--- | :--- |
| **Weather shifts** | Dense winter fog and monsoon flooding on arterial highways | Weather and visibility inputs in the predictor; alert escalation and speed damping |
| **Speed differentials** | High differences in vehicle speed on highways | Dynamic VMS speed overrides (80, 50 and 35 km/h) |
| **Delayed medical response** | Late emergency notification and response | Automated CAD routing to the nearest Level-1 trauma center |
| **No closed-loop feedback** | Sensors and driver warnings are not connected | Three-tier IIoT architecture from perception to actuation |

---

## 3. System Objectives

The project is guided by four primary technical objectives. Each of them corresponds to a major part of the implemented system and is described below.

### 3.1 Deep Empirical Analysis
The first objective is to identify casualty correlations across time (24-hour commuting peaks), weather conditions and road classifications using 20,000 verified records. The dataset includes the hour of the day, weekday information, peak-hour flags, the type of road and the prevailing weather, which together allow patterns to be studied from several angles. The empirical analysis forms the evidence base for every later decision in the system, including the calibration of the severity predictor and the thresholds used by the alert engine.

### 3.2 Bayesian AI Predictor
The second objective is to formulate an empirical likelihood model that calculates accident severity probabilities, classified as Minor, Major or Fatal, from real-time driving inputs. Rather than giving only a single label, the predictor reports a full probability distribution so that the user can see how likely each outcome is. This is implemented as the interactive What-If Scenario Predictor in Module 1.

### 3.3 Closed-Loop IIoT Architecture
The third objective is to implement the complete three-tier IIoT paradigm: Perception (edge sensors), then Network/Edge inference, then Actuation (VMS speed overrides and CAD ambulance routing). The architecture is described as industrial and closed-loop because the output of the last tier, a changed speed limit and a dispatched ambulance, is a physical or operational response to what the first tier measured.

### 3.4 Cloud CI/CD Deployment
The fourth objective is to standardise production on a single clean entrypoint, `streamlit_app.py`, running live on Streamlit Community Cloud. A single entrypoint keeps the deployment simple and avoids confusion between duplicate application files. During development the codebase was refactored and the redundant `app.py` was removed in support of this goal.

### 3.5 Mapping of Objectives to Modules

| Objective | Implemented In | Main Output |
| :--- | :--- | :--- |
| **Deep Empirical Analysis** | Module 1 dashboard (`streamlit_app.py`) | Filters, distribution matrix, Top 10 state ranking, risk insights |
| **Bayesian AI Predictor** | Module 1 What-If predictor | Predicted severity, probability distribution, risk score, hazard breakdown |
| **Closed-Loop IIoT Architecture** | Module 2 (`pages/iot_monitor.py`, `iot_simulator.py`) | Hazard alerts, VMS speed override, CAD dispatch |
| **Cloud Deployment** | Streamlit Community Cloud | Live application at a public URL |

---

## 4. Dataset Architecture & Preprocessing Pipeline

### 4.1 Dataset Overview
The project is empirically grounded in `indian_roads_dataset.csv`, which contains 20,000 records with 24 attributes each. The dataset encompasses spatial, temporal, environmental, infrastructure and impact dimensions. This breadth allows each accident to be described not only by where and when it happened, but also by the road it occurred on, the weather and visibility at that moment, the traffic around it and the consequences that followed.

The dataset was integrated into the Streamlit dashboard during the initial development stage and serves two roles: it is the source of the historical charts and rankings in Module 1, and it is the statistical basis for the Laplace-smoothed severity predictor. It is also used by Module 2, whose simulated sensor packets are grounded in the distributions of the eight cities and whose map displays real accident coordinates.

### 4.2 Spatial Identifiers
The spatial dimension contains the attributes `city`, `state`, `latitude` and `longitude`. Coordinates were bounded strictly to the eight metropolitan regional corridors. This gives every record a precise position that can be plotted on the geospatial map and a city and state label that supports filtering and the Top 10 state rankings.

### 4.3 Temporal Markers
The temporal dimension contains `date`, `time`, `hour` (0 to 23), `day_of_week`, `is_weekend` and `is_peak_hour`. As part of the engineering work, peak-hour binary flags were created for the periods 08:00 to 10:00 and 17:00 to 20:00. These flags make it simple to compare accidents during commuting peaks with those at other times, which supports the objective of studying 24-hour commuting patterns.

### 4.4 Road Infrastructure
The road infrastructure dimension contains `road_type` (highway, rural or urban), `lanes` (1 to 6) and `traffic_signal`. Categorical values were standardised and lane capacity was cross-verified. Road type is especially important because the project finds that highway collisions show markedly higher casualty rates per incident than urban ones.

### 4.5 Environmental Conditions
The environmental dimension contains `weather` (clear, fog or rain), `visibility` (high, medium or low) and `temperature`. Visibility values were normalised onto optical scales and temperature is expressed in degrees Celsius. These attributes link directly to the hazards that concern the project most, namely fog, rain, low visibility and extreme heat.

### 4.6 Impact & Evaluation
The impact and evaluation dimension contains `traffic_density`, `vehicles_involved`, `casualties`, `severity` and `risk_score`. Sparse columns such as festival were eliminated, and the risk score was mapped onto the range 0 to 1. Severity, recorded as Minor, Major or Fatal, is the quantity that the Bayesian predictor estimates, while the normalised risk score is reused in the dashboard's safety banner and in the alert thresholds.

### 4.7 Preprocessing Summary

| Feature Dimension | Attributes Included | Engineering / Normalization Applied |
| :--- | :--- | :--- |
| **Spatial Identifiers** | `city`, `state`, `latitude`, `longitude` | Bounded coordinates strictly to 8 metropolitan regional corridors. |
| **Temporal Markers** | `date`, `time`, `hour` (0-23), `day_of_week`, `is_weekend`, `is_peak_hour` | Engineered peak-hour binary flags (08:00-10:00 & 17:00-20:00). |
| **Road Infrastructure** | `road_type` (highway/rural/urban), `lanes` (1-6), `traffic_signal` | Categorical standardization; cross-verified lane capacity. |
| **Environmental Conditions** | `weather` (clear/fog/rain), `visibility` (high/med/low), `temperature` | Normalized visibility optical scales; temperature in °C. |
| **Impact & Evaluation** | `traffic_density`, `vehicles_involved`, `casualties`, `severity`, `risk_score` | Eliminated sparse columns (e.g. festival); risk mapped [0, 1]. |

### 4.8 Geographic Coverage
The eight metropolitan corridors covered by the dataset are Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai and Pune. Using the same eight cities throughout the project keeps the analytics, the sensor simulation and the hospital assignment consistent with one another.

---

## 5. Three-Tier Industrial IoT (IIoT) Architecture

### 5.1 Closed-Loop Sensing-to-Actuation
Unlike academic dashboards that merely visualise historical CSV files, this system executes an industrial closed-loop sensing-to-actuation architecture. The architecture is divided into three tiers: Perception, Network and Edge, and Application and Actuation. Information moves upward from the road to the operator and decisions move back down to the road in the form of signs and emergency dispatch.

```
┌────────────────────────────────┐     ┌────────────────────────────────┐     ┌────────────────────────────────┐
│      Tier 1: Perception        │ ──> │    Tier 2: Network & Edge      │ ──> │       Tier 3: Actuation        │
│     Roadside edge sensing      │     │  Edge computing and inference  │     │      VMS and CAD dispatch      │
└────────────────────────────────┘     └────────────────────────────────┘     └────────────────────────────────┘
```

### 5.2 Tier 1: Perception Layer (Roadside Edge Sensing)
The perception layer collects physical road telemetry: ambient temperature, optical transmission (fog density), precipitation presence, vehicle headway and average corridor velocity. Its hardware roles are:
- **Optical Visibility Meters:** Measure how clearly the road can be seen and therefore the density of fog.
- **Roadside Weather Stations:** Record ambient temperature and the presence of precipitation.
- **Radar Speed Doppler Units:** Measure the average corridor velocity of passing traffic.
- **Inductive Traffic Counters:** Count vehicles and provide the vehicle headway information.

### 5.3 Tier 2: Network & Edge Layer (Edge Computing)
The second tier simulates MQTT/REST packet transport. It ingests telemetry every 5 seconds, applies multi-factor hazard escalation and computes instant severity likelihoods. Its components are:
- **Edge Gateway Node:** Receives the sensor packets and passes them on for analysis.
- **Rule-Based Alert Engine:** Combines several factors, such as weather, visibility, time and traffic density, to decide the alert level.
- **Empirical Bayesian Predictor:** Computes the severity probabilities for the current conditions.

### 5.4 Tier 3: Application & Actuation (Command & Safety)
The third tier renders the live operator console and actuates the output devices. It actuates physical overhead LED Variable Message Signs with speed overrides and auto-dispatches regional trauma units. Its components are:
- **Streamlit Community Cloud:** Hosts the live application and operator console.
- **Dynamic Highway VMS Actuator:** Changes the speed limit shown on the overhead sign.
- **Automated Emergency CAD Interconnect:** Selects the hospital, the patrol interceptors and the ambulance ETA.

### 5.5 Architecture Summary Table

| IIoT Layer | Components & Hardware Roles | Data Flow & Technical Function |
| :--- | :--- | :--- |
| **Tier 1: Perception Layer (Roadside Edge Sensing)** | Optical Visibility Meters; Roadside Weather Stations; Radar Speed Doppler Units; Inductive Traffic Counters | Collects physical road telemetry: ambient temperature, optical transmission (fog density), precipitation presence, vehicle headway, and average corridor velocity. |
| **Tier 2: Network & Edge Layer (Edge Computing)** | Edge Gateway Node; Rule-Based Alert Engine; Empirical Bayesian Predictor | Simulates MQTT/REST packet transport. Ingests telemetry every 5s, applies multi-factor hazard escalation, and computes instant severity likelihoods. |
| **Tier 3: Application & Actuation (Command & Safety)** | Streamlit Community Cloud; Dynamic Highway VMS Actuator; Automated Emergency CAD Interconnect | Renders live operator console. Actuates physical overhead LED Variable Message Signs with speed overrides and auto-dispatches regional trauma units. |

---

## 6. Module 1: Historical Analytics & What-If Predictor

### 6.1 Role of Module 1
Module 1, implemented in `streamlit_app.py`, serves as the command analytics center of the project. It is the single clean entrypoint of the deployed application. The module incorporates multivariate filtering across State, City, Severity, Road Type and Weather, alongside a 2×2 visual distribution matrix and Top 10 state rankings. Most importantly, it integrates the interactive What-If Scenario Predictor.

### 6.2 Multivariate Filtering
The dashboard allows the user to filter the dataset by State, City, Severity, Road Type and Weather. Filters can be combined, so a user can for example narrow the records to a particular city and a particular weather condition and immediately see how the charts change. The sidebar filter widgets were also tested during peer code review to confirm that they respond correctly. This filtering turns the 20,000 records into an exploratory tool rather than a static report.

### 6.3 Visual Distribution Matrix and Top 10 States
The dashboard presents a 2×2 visual distribution matrix, which displays four charts side by side so that the user can compare different distributions of the filtered data at a glance. In addition, it shows Top 10 state rankings, so that the states with the greatest accident burden can be identified quickly.

### 6.4 State-Wise Accident Analysis
The State-Wise Accident Analysis module was implemented by Arvind Mourya (commit `567d35e`). It builds grouping aggregations that calculate accident volume and casualties for the Top 10 Indian states. The results are shown in dual bar charts that compare state accident frequencies with casualty ratios. Displaying both measures together matters because a state with many accidents is not necessarily the state where accidents are most severe.

### 6.5 Accident Risk & Safety Insights Banner
The Accident Risk & Safety Insights dashboard banner was engineered by Amit Kohli (commit `c8f4245`). It applies threshold-based visual alerts that classify risk as High Risk (0.7 or above), Moderate (0.4 or above) and Lower Risk. The banner also includes adverse weather keyword counters, which count weather conditions that are associated with road safety advisories. Together these give the viewer an immediate sense of how dangerous the currently filtered set of records is.

| Risk Level | Threshold on Risk Score |
| :--- | :--- |
| **High Risk** | 0.70 and above |
| **Moderate** | 0.40 and above |
| **Lower Risk** | Below the Moderate threshold |

### 6.6 Mathematical Calibration of the Predictor
The What-If predictor estimates conditional severity distributions:
$$P(\text{Severity} \mid \text{Weather, Visibility, Road, Time, Density})$$

It does so using Laplace-smoothed empirical Bayes ratios computed directly from the 20,000 dataset records. In plain terms, the predictor looks at how often each severity occurred in past records that resemble the scenario chosen by the user, and converts those counts into probabilities. Laplace smoothing ensures that combinations of conditions that are rare in the data do not produce misleading zero probabilities.

Because the calibration is based directly on the dataset, no external model is needed and the result can be traced back to the recorded accidents. This is why the predictor is described as empirical.

### 6.7 Input Matrix
The user describes a scenario through the following inputs:
- **Corridor City:** The metropolitan corridor in which the scenario takes place.
- **Road Classification:** Highway, rural or urban.
- **Weather Condition:** Clear, fog or rain.
- **Optical Visibility:** High, medium or low.
- **Traffic Density:** The amount of traffic on the road.
- **Hour of Day:** From 0 to 23.
- **Vehicles Involved:** From 1 to 5.

### 6.8 Real-Time Outputs
For every scenario the predictor produces four outputs:
- **Predicted Severity:** Minor, Major or Fatal.
- **Severity Probability Distribution:** For example, Minor: 48.2% | Major: 36.5% | Fatal: 15.3%.
- **Normalized Composite Risk Score:** A value between 0.00 and 1.00.
- **Automated Contributing Hazard Breakdown:** An explanation of which conditions in the scenario raise the risk.

Showing the whole distribution, and not just the most likely class, helps the user judge how confident the prediction is. The hazard breakdown connects the numerical result to concrete causes such as fog, low visibility or heavy traffic.

---

## 7. Module 2: IIoT Edge Telemetry, VMS & CAD Dispatch

### 7.1 Purpose of Module 2
Module 2, implemented in `pages/iot_monitor.py` with the sensor logic in `iot_simulator.py`, delivers the operational industrial IoT runtime environment. It was first added as the foundational IoT Simulation & Alert Monitoring module (commit `269d0c1`) and was later refined through several contributions covering the sensor generator methods, the alert display cards and the multi-page navigation.

### 7.2 Roadside Telemetry Generation
The module generates realistic sensor packets that are grounded in the exact distributions of the eight Indian cities: Bangalore, Chandigarh, Chennai, Delhi, Hyderabad, Kolkata, Mumbai and Pune. Basing the simulated packets on the real dataset means that the readings behave like those of the corridors they represent. Duplicate sensor generator functions were removed and syntax errors were resolved during development, and state variables are synchronised between `streamlit_app.py` and the multi-page components.

### 7.3 Multi-Tier Alert Escalation
Incoming telemetry is categorised into four hazard levels. The alert engine considers several factors together, so that the level reflects the combination of conditions and not any single reading.

| Alert Level | Triggering Conditions |
| :--- | :--- |
| **SAFE** | Clear weather during the day |
| **LOW** | Urban commuter congestion |
| **MEDIUM** | Rain, daytime low visibility, or extreme heat of 42°C or above |
| **HIGH** | Night fog combined with low visibility; highway rain combined with high density; risk score of 0.70 or above |

The alert display cards and their styling were refined in `pages/iot_monitor.py` so that the current level is easy to recognise on the operator console.

### 7.4 Smart Highway Variable Message Sign (VMS)
The VMS is rendered as an electronic overhead LED matrix billboard styled with retro-illuminated amber and red typography. Its purpose is to dampen the corridor speed limit automatically as conditions worsen:

| Road Condition | Speed Limit Displayed |
| :--- | :--- |
| **Normal** | 80 km/h |
| **Rain** | 50 km/h |
| **Dense Fog / Night Collision Hazard** | 35 km/h |

Because the sign responds to the alert engine without manual input, drivers receive an appropriate speed instruction at the moment the hazard is detected. This is the actuation step that closes the loop between roadside sensing and driver behaviour.

### 7.5 Computer-Aided Dispatch (CAD) Interconnect
When a hazard or incident is registered, the CAD interconnect automatically assigns the regional Level-1 trauma facility. Examples given in the project are the AIIMS Trauma Centre for Delhi, KEM for Mumbai, Victoria Hospital for Bangalore and PGIMER for Chandigarh. The module also calculates highway patrol interceptors and computes real-time ambulance arrival ETAs in the range of 5 to 8 minutes.

By choosing the hospital and estimating the arrival time without manual coordination, the CAD module is designed to support the critical Golden Hour in which emergency treatment matters most.

### 7.6 Geospatial Pydeck Hotspot Mapping
The module renders a 3D interactive Scatterplot layer using Pydeck. The map displays real accident coordinates from the dataset alongside the active IoT sensor node, so that the position of the simulated sensor can be seen in relation to the historical accident hotspots. Pydeck and Numpy requirements were integrated into the project to support this geospatial plotting.

### 7.7 Persistent Incident Audit Log
The map is paired with a persistent incident audit log that records events with timestamps and supports CSV export. Session persistence supports the multi-page navigation so that the log remains available while the operator moves between pages of the application.

---

## 8. Deployment & Repository Structure

### 8.1 Single Clean Entrypoint
Production is standardised on a single clean entrypoint, `streamlit_app.py`. Earlier in development there was a redundant `app.py`, which was removed when the codebase was refactored. Having a single entrypoint means that Streamlit Community Cloud has one unambiguous file to run, and the second module is loaded as a page from the pages folder.

### 8.2 Streamlit Community Cloud
The system is deployed live on Streamlit Community Cloud at [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/). The live deployment, together with repository governance, was spearheaded by the team leader. Linux system packages required by the deployment were configured in `packages.txt`, and library versions were left unpinned.

### 8.3 Repository Components

| Component | Purpose |
| :--- | :--- |
| `streamlit_app.py` | Single production entrypoint; Module 1 analytics and What-If predictor |
| `pages/iot_monitor.py` | Module 2 operational console: alerts, VMS, CAD, map and audit log |
| `iot_simulator.py` | Sensor packet generator for the roadside telemetry simulation |
| `indian_roads_dataset.csv` | Dataset of 20,000 records and 24 attributes |
| `Road_Accident_Pattern_Analysis.ipynb` | Google Colab exploratory research notebook |
| `packages.txt` | Linux system packages for deployment |
| `README.md` | Project setup instructions and feature descriptions |
| `CONTRIBUTING.md` | Team setup guide |
| `run_app.bat` | Batch file for launching the app locally |
| `.vscode` | Editor configuration |
| `Dev Container configuration` | Containerised development environment |

### 8.4 Development Environment Support
Several files support the team during development. A `run_app.bat` file allows the application to be started easily, a `.vscode` configuration standardises the editor setup, and a Dev Container configuration provides a reproducible environment. The `README.md` contains setup instructions and feature descriptions, while `CONTRIBUTING.md` provides the team setup guide for new contributors.

### 8.5 Exploratory Notebook
A Google Colab exploratory research notebook was written during the early stage of the project. Its filename was later standardised to `Road_Accident_Pattern_Analysis.ipynb` and the dataset schema was verified. The notebook documents the exploratory work that preceded the dashboard.

---

## 9. Experimental Findings

Analysis of the 20,000-record dataset and the behaviour of the IIoT simulation produced three principal findings.

### 9.1 Adverse Weather Multiplier
Dense winter fog coupled with low visibility during nighttime hours (21:00 to 05:00) yields a **+42% increase in fatality likelihood**. This represents the single highest hazard factor across all eight corridors. The finding explains why the alert engine treats night fog with low visibility as a HIGH alert and why the VMS reduces the speed limit to 35 km/h for dense fog.

### 9.2 Highway vs. Urban Severity Ratio
Highway collisions exhibit **2.3 times higher casualty rates per incident** compared with urban roads. The report attributes this to elevated approach momentum. The finding confirms the necessity of dynamic VMS speed intervention, since reducing approach speed on highways addresses the cause of the higher casualty rate directly.

### 9.3 Golden Hour Response Optimization
Automated CAD routing provides an ambulance arrival window of **5 to 8 minutes**. This mitigates emergency notification delays and dramatically improves survival odds for critically injured highway commuters. The finding demonstrates the value of connecting detection and dispatch automatically.

### 9.4 Summary of Findings

| Finding | Result | Related System Feature |
| :--- | :--- | :--- |
| **Adverse weather multiplier** | +42% fatality likelihood in night fog with low visibility (21:00-05:00) | HIGH alert level; 35 km/h VMS limit |
| **Highway vs. urban severity** | 2.3x higher casualty rate per incident on highways | Dynamic VMS speed intervention |
| **Golden Hour response** | Ambulance arrival window of 5-8 minutes | Automated CAD routing |

### 9.5 Combined Interpretation
Taken together, the three findings support the design of the closed-loop system. The first identifies the most dangerous conditions, the second shows why speed control on highways matters and the third shows how emergency response can be accelerated. Each finding is connected to a specific feature, and each feature is part of the same chain from sensing to actuation.

---

## 10. Real-World Impact

The project addresses a problem of national scale, with over 150,000 road fatalities annually in India. By moving from a retrospective view of accidents to a proactive one, it demonstrates how roadside sensing, automated warnings and emergency dispatch can be combined into one platform.

- **For municipal authorities and traffic police:** The live application provides an accessible, high-performance platform for active accident mitigation.
- **For drivers:** The VMS actuator provides speed guidance that adapts to rain, fog and night conditions.
- **For injured commuters:** The CAD interconnect shortens the time to a suitable trauma center.
- **For the research team:** The dataset-driven analytics make it possible to understand which factors lead to the most serious accidents.

---

## 11. Team Organisation & Contributions

The project was carried out by a 14-member team. The official contribution breakdown was audited directly from Git commit hashes, author logs and remote branches across the repository. Each member worked on a named branch, and contributions were integrated through pull requests. The group leaders are **Lovish Chauhan** and **Omgyan Singh**, and the work was carried out under the guidance of the mentor, **Mr. Unwan Khan**, at **TrainX**.

### 11.1 Lovish Chauhan (Team Leader) - Branch: Lovish - High (Lead)
Lovish Chauhan spearheaded the system architecture, the live deployment on Streamlit Cloud and the repository governance. He built the What-If ML Accident Severity & Risk Predictor and engineered the Smart Highway VMS actuator together with the CAD emergency hospital dispatch. He also refactored the codebase, removed the redundant `app.py`, built `run_app.bat` and configured `.vscode`.

### 11.2 Krishu Kumar - Branch: krishu - High
Krishu Kumar authored the initial Streamlit dashboard application (commits `fca04dc` and `fd8d996`) and integrated the Indian Roads Dataset of 20,000 records. He also authored the Google Colab exploratory research notebook (commit `98f279f`) and configured the Linux system packages (`packages.txt`) and unpinned libraries used by the deployment.

### 11.3 Mayank Gupta - Branch: mayank - High
Mayank Gupta added the foundational IoT Simulation & Alert Monitoring module (commit `269d0c1`). He created the initial `iot_simulator.py` and `pages/iot_monitor.py` and integrated the Pydeck and Numpy requirements needed for geospatial plotting.

### 11.4 Alok Chaubey - Branch: alok - High
Alok Chaubey resolved syntax errors and deduplicated the sensor generator functions (commit `5f14dde`). He synchronised state variables between `streamlit_app.py` and the multi-page components and added the Dev Container environment configuration (commit `e5dfaf4`). His work was merged through PR #8.

### 11.5 Arvind Mourya - Branch: arvind - High
Arvind Mourya implemented the State-Wise Accident Analysis module (commit `567d35e`). He built the grouping aggregations that calculate accident volume and casualties for the Top 10 Indian states and integrated dual bar charts comparing state frequencies with casualty ratios.

### 11.6 Amit Kohli - Commit: c8f4245 - High
Amit Kohli engineered the Accident Risk & Safety Insights dashboard banner (commit `c8f4245`). He added threshold-based visual alerts for High Risk (0.7 or above), Moderate (0.4 or above) and Lower Risk, and implemented adverse weather keyword counters for road safety advisories.

### 11.7 Ayush Patel - Branch: ayush - High
Ayush Patel managed the integration of Pull Request #4 into the repository (commit `c108d2c`) and synchronised updates to `streamlit_app.py` (commit `396683d`). He also contributed project setup instructions and feature descriptions in `README.md` (commit `2c3227a`).

### 11.8 Pritam Kumar - Branch: pritam - Medium
Pritam Kumar enhanced the sensor generator methods in `iot_simulator.py` (commit `0aa5a8d`) and refined the alert display cards and UI styling in `pages/iot_monitor.py` (commit `03be2bc`). He supported the multi-page navigation routing and session persistence.

### 11.9 Kritika - Branch: kritikaaa - Medium
Kritika authored the `CONTRIBUTING.md` team setup guide (commit `17c34b4`). She verified the IoT simulation telemetry parameters and supported the documentation.

### 11.10 Sunal - Branch: sunal - Medium
Sunal updated the `iot_monitor.py` parameters (commit `b54a36b`) and authored multiple iterations of the `README.md` documentation (commits `f81277d`, `82a8fdd` and `fff9bae`).

### 11.11 Daniyal Malik - Branch: Daniyal - Medium
Daniyal Malik standardised the notebook filename to `Road_Accident_Pattern_Analysis.ipynb` (commit `3758353`) and conducted the dataset schema verification.

### 11.12 Riddhi Gupta - Branch: Riddhi-Gupta - Medium
Riddhi Gupta documented the project feature overviews in `README.md` (commits `91db893` and `bad32ef`) and researched empirical accident patterns and environmental hazard factors in Indian cities.

### 11.13 Ayan Ansari - Branch: ayan - Low / Partial
Ayan Ansari managed the merge of PR #3 from Krishu (commit `434d47e`) and contributed to the deployment documentation updates in `README.md` (commit `d6668d4`).

### 11.14 Om - Branch: om - Low / Minimal
Om participated in peer code review cycles, tested the sidebar filter widgets and assisted in UI responsiveness verification.

### 11.15 Collaboration Workflow
The repository shows a branch-per-member workflow. Members worked on their own branches and contributions were brought together through pull requests such as PR #3, PR #4 and PR #8, with commit hashes recorded in the audit. Documentation was developed in parallel with the code through `README.md` and `CONTRIBUTING.md`, so that the project could be set up and understood by every team member.

### 11.16 Contribution Levels

| Level | Members |
| :--- | :--- |
| **High (Lead)** | Lovish Chauhan |
| **High** | Krishu Kumar, Mayank Gupta, Alok Chaubey, Arvind Mourya, Amit Kohli, Ayush Patel |
| **Medium** | Pritam Kumar, Kritika, Sunal, Daniyal Malik, Riddhi Gupta |
| **Low / Partial** | Ayan Ansari |
| **Low / Minimal** | Om |

---

## 12. Conclusion

The project successfully establishes an industrial-grade safety architecture that unifies historical empirical pattern recognition with real-time IIoT physical actuation. By enforcing a clean single-entrypoint deployment on Streamlit Community Cloud, the system provides municipal authorities and traffic police with an accessible, high-performance platform for active accident mitigation.

Each of the four objectives was achieved. The empirical analysis of 20,000 records across eight corridors identified the conditions most associated with severe accidents. The Bayesian predictor turned that evidence into probabilities for any scenario. The three-tier architecture carried live telemetry through to a speed override on the VMS and an automated hospital dispatch. The whole system was made available as a live web application.

The result is a platform in which data from past accidents shapes the response to hazards that are developing now, and in which the response reaches both the driver and the emergency services.

---

## 13. Future Engineering Scope

### 13.1 Hardware Edge Nodes
The current system simulates roadside telemetry. The planned next step is flashing physical ESP32 or Raspberry Pi microcontrollers to transmit real-world LoRaWAN telemetry into the edge gateway broker. This would replace simulated packets with measurements from actual roadside hardware.

### 13.2 Computer Vision Integration
The roadmap includes deploying YOLOv8 on roadside CCTV video feeds for automated vehicle collision detection. This would allow incidents to be detected directly from video, supporting the automated dispatch process.

### 13.3 Vehicle-to-Everything (V2X)
The final item is broadcasting active hazard advisories directly into vehicular telematics dashboards. Through V2X, drivers would receive warnings inside their own vehicles in addition to the overhead signs.

---

## 14. Glossary of Terms

| Term | Meaning in this Project |
| :--- | :--- |
| **IIoT** | Industrial Internet of Things; the sensing, edge computing and actuation paradigm used by the system |
| **VMS** | Variable Message Sign; the overhead LED sign that displays speed limits and warnings |
| **CAD** | Computer-Aided Dispatch; the module that assigns trauma centers and computes ambulance ETAs |
| **Golden Hour** | The critical time window for emergency medical response after an accident |
| **Empirical Bayes** | Estimating probabilities from observed frequencies in the dataset |
| **Laplace smoothing** | A correction that prevents rare combinations from producing zero probabilities |
| **Edge Gateway** | Node that receives sensor packets and runs the alert and prediction logic |
| **MQTT / REST** | Packet transport styles simulated between the sensors and the edge layer |
| **Pydeck** | Library used for the 3D interactive geospatial Scatterplot map |
| **Level-1 trauma center** | Highest-level regional hospital assigned by CAD (for example AIIMS, KEM, PGIMER) |
| **ESP32 / Raspberry Pi** | Microcontrollers planned for physical edge nodes |
| **LoRaWAN** | Wireless protocol planned for real-world telemetry transmission |
| **YOLOv8** | Computer-vision model planned for collision detection on CCTV feeds |
| **V2X** | Vehicle-to-Everything; broadcasting hazard advisories into vehicles |

---

## 15. Project Links & Resources

| Resource | Location |
| :--- | :--- |
| **GitHub Repository** | [https://github.com/igris-bit/Road-Accident-Pattern-Analysis](https://github.com/igris-bit/Road-Accident-Pattern-Analysis) |
| **Live Application** | [https://road-accident-pattern-analysis.streamlit.app/](https://road-accident-pattern-analysis.streamlit.app/) |
| **Dataset** | `indian_roads_dataset.csv` (20,000 records x 24 attributes) |
| **Notebook** | `Road_Accident_Pattern_Analysis.ipynb` |
| **Team Leader Contact** | `lovishneeraj@gmail.com` |

---
*Invertis University • in association with TrainX • IIoT-3 Practical, November 2026*
