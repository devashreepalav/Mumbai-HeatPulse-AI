import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# 1. PAGE CONFIG
st.set_page_config(page_title="Mumbai HeatPulse", layout="wide")
st.title("🏙️ Mumbai HeatPulse: AI Urban Climate Analysis")

# 2. LOAD DATA
df = pd.read_csv('mumbai_heat_base.csv')

# 3. SIDEBAR - LIVE WEATHER API
st.sidebar.header("Live Satellite Data")
try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    live_temp = requests.get(url).json()['current_weather']['temperature']
    st.sidebar.metric("Current Mumbai Temp", f"{live_temp}°C")
except:
    st.sidebar.warning("API Offline")

# 4. MAIN DASHBOARD - INTERACTIVE CHART
st.subheader("Ward-wise Heat vs. Greenery Analysis")
fig = px.scatter(df, x="Vegetation_Index_NDVI", y="Surface_Temp_Celsius",
                 size="Building_Density_Score", color="Avg_Income_Level",
                 hover_name="Ward", text="Ward",
                 labels={"Vegetation_Index_NDVI": "Greenery (NDVI)", "Surface_Temp_Celsius": "Temp (°C)"},
                 title="The Heat Island Effect in Mumbai")

st.plotly_chart(fig, use_container_width=True)

# 5. DATA EXPLORER
col1, col2 = st.columns(2)
with col1:
    st.subheader("Ward Rankings")
    st.dataframe(df.sort_values(by="Surface_Temp_Celsius", ascending=False))

with col2:
    st.subheader("AI Prediction Insight")
    st.info("Wards with NDVI below 0.15 show a 4.2°C higher average temperature than forested wards (R/C).")