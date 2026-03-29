import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# 1. PAGE SETUP
st.set_page_config(page_title="Mumbai HeatPulse Pro AI", layout="wide", page_icon="🌡️")
st.title("🏙️ Mumbai HeatPulse: Strategic Urban Climate Intelligence")

# 2. DATA LOADING & AI CALCULATIONS
@st.cache_data
def get_data():
    df = pd.read_csv('mumbai_heat_base.csv')
    
    # IDEA 1: HEAT VULNERABILITY INDEX
    # We create a normalized 0-100 score where higher = more risk
    df['Vulnerability_Index'] = (
        (df['Surface_Temp_Celsius'] * 0.5) + 
        (df['Building_Density_Score'] * 0.3) - 
        (df['Vegetation_Index_NDVI'] * 10)
    ).rank(pct=True) * 100
    return df

df = get_data()

# 3. SIDEBAR SIMULATOR & LIVE WEATHER
st.sidebar.header("🕹️ Simulation Tools")

# IDEA 2: "WHAT-IF" PLANNING SLIDER
st.sidebar.subheader("Urban Forestry Simulator")
tree_boost = st.sidebar.slider("Increase Ward Canopy (NDVI boost)", 0.0, 0.3, 0.0)
cooling_effect = tree_boost * 12.5 # Simulated logic: 0.1 NDVI = -1.25°C reduction

st.sidebar.info(f"Predicted Cooling: -{cooling_effect:.1f}°C")

try:
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    live_temp = requests.get(url, timeout=5).json()['current_weather']['temperature']
    st.sidebar.metric("Live Mumbai Temp", f"{live_temp}°C")
except:
    st.sidebar.warning("Live Weather API Offline")

# 4. MAIN DASHBOARD - INTERACTIVE MAP (IDEA 3)
st.subheader("📍 Ward-Level Heat Vulnerability Map")
# This uses your new Latitude and Longitude columns
fig_map = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", 
                         color="Vulnerability_Index", size="Surface_Temp_Celsius",
                         hover_name="Ward", color_continuous_scale="OrRd",
                         zoom=10, height=500)
fig_map.update_layout(mapbox_style="carto-positron")
st.plotly_chart(fig_map, use_container_width=True)

# 5. ANALYSIS CHARTS
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📈 Heat Island Correlation")
    simulated_df = df.copy()
    simulated_df['Surface_Temp_Celsius'] -= cooling_effect
    
    fig_scatter = px.scatter(simulated_df, x="Vegetation_Index_NDVI", y="Surface_Temp_Celsius",
                         size="Building_Density_Score", color="Vulnerability_Index",
                         hover_name="Ward", color_continuous_scale="RdYlGn_r")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col2:
    st.subheader("🤖 AI Priority Alert")
    critical_ward = df.loc[df['Vulnerability_Index'].idxmax(), 'Ward']
    st.error(f"**High Risk:** {critical_ward} requires immediate cooling intervention.")
    
    st.subheader("📥 Export Data")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Full Analysis", data=csv, file_name='mumbai_heat_pro.csv')
