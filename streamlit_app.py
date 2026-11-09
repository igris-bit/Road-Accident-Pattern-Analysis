import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Road Accident Pattern Analysis",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
<style>
    .metric-box {
        background-color: #f0f2f6;
        border-radius: 8px;
        padding: 15px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_data():
    """Load and clean the Indian roads accident dataset."""
    df = pd.read_csv("indian_roads_dataset.csv")
    if "festival" in df.columns:
        df = df.drop(columns=["festival"])
    df = df.drop_duplicates()
    df = df.dropna()
    return df


# Load dataset
try:
    df_raw = load_data()
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ----------------- SIDEBAR FILTERS -----------------
st.sidebar.title("🔍 Filter Accidents")

# State filter
all_states = sorted(df_raw["state"].dropna().unique().tolist())
selected_state = st.sidebar.selectbox("Select State", ["All"] + all_states)

# Filter by state first to populate cities
if selected_state != "All":
    state_df = df_raw[df_raw["state"] == selected_state]
else:
    state_df = df_raw

all_cities = sorted(state_df["city"].dropna().unique().tolist())
selected_city = st.sidebar.selectbox("Select City", ["All"] + all_cities)

# Severity filter
severity_options = sorted(df_raw["accident_severity"].dropna().unique().tolist())
selected_severity = st.sidebar.multiselect(
    "Accident Severity",
    options=severity_options,
    default=severity_options
)

# Weather filter
weather_options = sorted(df_raw["weather"].dropna().unique().tolist())
selected_weather = st.sidebar.multiselect(
    "Weather Condition",
    options=weather_options,
    default=weather_options
)

# Road type filter
road_options = sorted(df_raw["road_type"].dropna().unique().tolist())
selected_road = st.sidebar.multiselect(
    "Road Type",
    options=road_options,
    default=road_options
)

# Apply filters
df = df_raw.copy()

if selected_state != "All":
    df = df[df["state"] == selected_state]

if selected_city != "All":
    df = df[df["city"] == selected_city]

if selected_severity:
    df = df[df["accident_severity"].isin(selected_severity)]

if selected_weather:
    df = df[df["weather"].isin(selected_weather)]

if selected_road:
    df = df[df["road_type"].isin(selected_road)]

# ----------------- MAIN DASHBOARD -----------------
st.title("🚗 Road Accident Pattern Analysis Dashboard")
st.markdown("Interactive analysis of accident patterns, environmental factors, and severity distributions across Indian roads.")

st.markdown("---")

# ----------------- METRIC CARDS -----------------
total_accidents = len(df)
total_casualties = int(df["casualties"].sum()) if "casualties" in df.columns else 0
fatal_accidents = len(df[df["accident_severity"] == "fatal"])
fatal_pct = (fatal_accidents / total_accidents * 100) if total_accidents > 0 else 0
avg_risk = df["risk_score"].mean() if "risk_score" in df.columns else 0.0

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Accidents", f"{total_accidents:,}")
with col2:
    st.metric("Total Casualties", f"{total_casualties:,}")
with col3:
    st.metric("Fatal Accidents", f"{fatal_accidents:,}", f"{fatal_pct:.1f}%")
with col4:
    st.metric("Avg Risk Score", f"{avg_risk:.2f}")

st.markdown("---")

if total_accidents == 0:
    st.warning("No records match the selected filter criteria. Please adjust your filters.")
    st.stop()

# ----------------- VISUALIZATIONS (2x2 GRID) -----------------
st.subheader("📊 Accident Distribution & Factors")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
sns.set_theme(style="whitegrid")

# Chart 1: Time-based (Accidents by Hour)
sns.countplot(ax=axes[0, 0], data=df, x="hour", color="steelblue")
axes[0, 0].set_title("1. Accidents by Hour of the Day", fontsize=14, fontweight="bold")
axes[0, 0].set_xlabel("Hour (24-hour format)", fontsize=11)
axes[0, 0].set_ylabel("Number of Accidents", fontsize=11)

# Chart 2: Category-based (Accidents by Weather)
weather_order = df["weather"].value_counts().index
sns.countplot(ax=axes[0, 1], data=df, x="weather", order=weather_order, palette="Set2", hue="weather", legend=False)
axes[0, 1].set_title("2. Accidents by Weather Condition", fontsize=14, fontweight="bold")
axes[0, 1].set_xlabel("Weather", fontsize=11)
axes[0, 1].set_ylabel("Number of Accidents", fontsize=11)

# Chart 3: Category-based (Accidents by Severity)
severity_order = ["minor", "major", "fatal"]
available_severity = [s for s in severity_order if s in df["accident_severity"].unique()]
sns.countplot(ax=axes[1, 0], data=df, x="accident_severity", order=available_severity, palette="pastel", hue="accident_severity", legend=False)
axes[1, 0].set_title("3. Accidents by Severity Level", fontsize=14, fontweight="bold")
axes[1, 0].set_xlabel("Severity", fontsize=11)
axes[1, 0].set_ylabel("Number of Accidents", fontsize=11)

# Chart 4: Category-based (Accidents by Road Type)
road_order = df["road_type"].value_counts().index
sns.countplot(ax=axes[1, 1], data=df, x="road_type", order=road_order, palette="magma", hue="road_type", legend=False)
axes[1, 1].set_title("4. Accidents by Road Type", fontsize=14, fontweight="bold")
axes[1, 1].set_xlabel("Road Type", fontsize=11)
axes[1, 1].set_ylabel("Number of Accidents", fontsize=11)

plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

# ----------------- SUMMARY TABLES & OBSERVATIONS -----------------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📋 Summary Statistics")
    tab1, tab2 = st.tabs(["Severity Breakdown", "Weather Breakdown"])

    with tab1:
        severity_counts = df["accident_severity"].value_counts().reset_index()
        severity_counts.columns = ["Severity", "Total Accidents"]
        severity_counts["Percentage (%)"] = (severity_counts["Total Accidents"] / len(df) * 100).round(2)
        st.dataframe(severity_counts, use_container_width=True, hide_index=True)

    with tab2:
        weather_counts = df["weather"].value_counts().reset_index()
        weather_counts.columns = ["Weather", "Total Accidents"]
        weather_counts["Percentage (%)"] = (weather_counts["Total Accidents"] / len(df) * 100).round(2)
        st.dataframe(weather_counts, use_container_width=True, hide_index=True)

with col_right:
    st.subheader("💡 Key Insights & Observations")
    st.markdown("""
    - **Time-based Patterns**: Accident frequency shows distinct peaks across the 24-hour cycle, often correlating with peak commuting and low-visibility nighttime hours.
    - **Weather Impact**: Accidents are spread across clear, rain, and fog conditions. Adverse conditions contribute substantially to severe outcomes.
    - **Severity Distribution**: Minor incidents account for the largest proportion (>50%), while major and fatal incidents constitute critical areas for safety intervention.
    
    **Cautious Prevention Questions for Further Investigation:**
    - Could improved street lighting or traffic pacing during high-incident hours help reduce accident frequency?
    - Do specific weather conditions (e.g., heavy rain, dense fog) warrant dynamic speed limits on high-risk road segments?
    """)

st.markdown("---")

# ----------------- RAW DATA PREVIEW -----------------
with st.expander("🔍 View Raw / Filtered Dataset"):
    st.dataframe(df.head(100), use_container_width=True)
    csv_data = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv_data,
        file_name="filtered_accident_data.csv",
        mime="text/csv"
    )

# ----------------- STATE-WISE ACCIDENT ANALYSIS -----------------

st.markdown("---")
st.subheader("🏙️ Top 10 States by Road Accidents")

state_analysis = (
    df.groupby("state")
    .agg(
        Total_Accidents=("state", "count"),
        Total_Casualties=("casualties", "sum")
    )
    .sort_values(by="Total_Accidents", ascending=False)
    .head(10)
    .reset_index()
)

col1, col2 = st.columns(2)

with col1:
    st.write("### Accident Count by State")
    st.bar_chart(
        state_analysis.set_index("state")["Total_Accidents"]
    )

with col2:
    st.write("### Casualties by State")
    st.bar_chart(
        state_analysis.set_index("state")["Total_Casualties"]
    )

st.dataframe(state_analysis, use_container_width=True)


# ----------------- ACCIDENT RISK & SAFETY INSIGHTS -----------------

st.markdown("---")
st.subheader("🛡️ Accident Risk & Safety Insights")

if "risk_score" in df.columns and not df.empty:
    current_risk = df["risk_score"].mean()

    if current_risk >= 0.7:
        st.error("⚠️ High Risk: Extra caution is recommended in the selected conditions.")
    elif current_risk >= 0.4:
        st.warning("⚠️ Moderate Risk: Stay alert and maintain safe distance.")
    else:
        st.success("✅ Lower Risk: Continue following road safety rules.")

    st.metric("Filtered Average Risk", f"{current_risk:.2f}")

    if "weather" in df.columns:
        adverse_weather = df["weather"].astype(str).str.lower().isin(
            ["rain", "fog", "storm", "heavy rain"]
        ).sum()

        st.info(
            f"Weather-related records in current selection: {adverse_weather}. "
            "Drivers should reduce speed and maintain safe distance in poor visibility."
        )

    st.caption(
        "These are descriptive insights from historical records, "
        "not real-time predictions or causal conclusions."
    )

# ----------------- WHAT-IF ACCIDENT SEVERITY & RISK CALCULATOR -----------------

st.markdown("---")
st.subheader("🧠 What-If Accident Severity & Risk Predictor")
st.markdown(
    "Simulate custom driving scenarios and evaluate estimated accident risk & severity "
    "calibrated directly from the **20,000 Indian Road Accident records**."
)

calc_col1, calc_col2 = st.columns(2)

with calc_col1:
    all_cities_avail = sorted(df_raw["city"].dropna().unique().tolist())
    p_city = st.selectbox("Scenario City", options=all_cities_avail, key="pred_city")
    p_road = st.selectbox("Road Type", options=["highway", "urban", "rural"], key="pred_road")
    p_weather = st.selectbox("Weather Condition", options=["clear", "fog", "rain"], key="pred_weather")
    p_vis = st.selectbox("Visibility Level", options=["high", "medium", "low"], key="pred_vis")

with calc_col2:
    p_density = st.selectbox("Traffic Density", options=["low", "medium", "high"], key="pred_density")
    p_hour = st.slider("Hour of the Day (24-hour)", min_value=0, max_value=23, value=20, key="pred_hour")
    p_vehicles = st.slider("Vehicles Involved", min_value=1, max_value=5, value=2, key="pred_vehicles")

try:
    from iot_simulator import predict_accident_severity
    prediction = predict_accident_severity(
        df=df_raw,
        city=p_city,
        weather=p_weather,
        visibility=p_vis,
        road_type=p_road,
        traffic_density=p_density,
        hour=p_hour,
        vehicles_involved=p_vehicles
    )

    pred_col1, pred_col2, pred_col3 = st.columns(3)

    severity_badge = {
        "minor": "🟢 Minor Incident",
        "major": "🟡 Major Collision",
        "fatal": "🔴 Fatal Accident"
    }

    with pred_col1:
        st.metric(
            "Predicted Severity",
            severity_badge.get(prediction["predicted_severity"], prediction["predicted_severity"].upper())
        )

    with pred_col2:
        st.metric(
            "Estimated Risk Index",
            f"{prediction['risk_score']:.2f}",
            f"{prediction['risk_level']} Risk Level"
        )

    with pred_col3:
        st.markdown("**Probability Distribution:**")
        p_dist = prediction["probabilities"]
        st.write(f"• Minor: **{p_dist['minor']}%** | Major: **{p_dist['major']}%** | Fatal: **{p_dist['fatal']}%**")

    st.info(f"**Identified Contributing Factors:** {' • '.join(prediction['contributors'])}")

except Exception as e:
    st.warning(f"Predictor module initialized: {e}")

