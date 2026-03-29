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
    try:
        df = pd.read_csv('mumbai_heat_base.csv')
        # CLEANUP: Remove any hidden spaces in column names
        df.columns = df.columns.str.strip()
        
        # CALCULATE VULNERABILITY INDEX
        # Formula: High Temp + High Density - High Greenery
        df['Vulnerability_Index'] = (
            (df['Surface_Temp_Celsius'] * 0.5) + 
            (df['Building_Density_Score'] * 0.3) - 
            (df['Vegetation_Index_NDVI'] * 10)
        ).rank(pct=True) * 100
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = get_data()

if df is not None:
    # 3. SIDEBAR SIMULATOR & LIVE WEATHER
    st.sidebar.header("🕹️ Simulation Tools")
    
    st.sidebar.subheader("Urban Forestry Simulator")
    tree_boost = st.sidebar.slider("Increase Ward Canopy (NDVI boost)", 0.0, 0.3, 0.0)
    cooling_effect = tree_boost * 12.5 # Simulated logic: 0.1 NDVI = -1.25°C reduction
    st.sidebar.info(f"Predicted Cooling: -{cooling_effect:.1f}°C")

    try:
        url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
        live_data = requests.get(url, timeout=5).json()
        live_temp = live_data['current_weather']['temperature']
        st.sidebar.metric("Live Mumbai Temp", f"{live_temp}°C")
    except:
        st.sidebar.warning("Weather API Offline")

    # 4. MAIN DASHBOARD - GEOSPATIAL MAP
    st.subheader("📍 Ward-Level Heat Vulnerability Map")
    fig_map = px.scatter_mapbox(df, 
                             lat="Latitude", 
                             lon="Longitude", 
                             color="Vulnerability_Index", 
                             size="Surface_Temp_Celsius",
                             hover_name="Ward", 
                             color_continuous_scale="OrRd",
                             zoom=10, 
                             height=500)
    fig_map.update_layout(mapbox_style="carto-positron")
    st.plotly_chart(fig_map, use_container_width=True)

    # 5. ANALYSIS & SIMULATION CHART
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📈 Simulated Heat vs. Greenery")
        simulated_df = df.copy()
        simulated_df['Surface_Temp_Celsius'] -= cooling_effect
        
        fig_scatter = px.scatter(simulated_df, 
                             x="Vegetation_Index_NDVI", 
                             y="Surface_Temp_Celsius",
                             size="Building_Density_Score", 
                             color="Vulnerability_Index",
                             hover_name="Ward", 
                             color_continuous_scale="RdYlGn_r",
                             labels={"Surface_Temp_Celsius": "Temp (°C)"})
        st.plotly_chart(fig_scatter, use_container_width=True)

    with col2:
        st.subheader("🤖 AI Priority Alert")
        critical_ward = df.loc[df['Vulnerability_Index'].idxmax(), 'Ward']
        st.error(f"**High Risk:** Ward {critical_ward} requires immediate cooling.")
        
        st.subheader("📥 Export Data")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV Report", data=csv, file_name='mumbai_heat_pro.csv')

# 6. STRATEGIC ADVISOR (FINAL PRO FEATURE)
st.markdown("---")
st.subheader("📋 Ward-Specific Heat Action Plan")

selected_ward = st.selectbox("Select a Ward to generate a Mitigation Strategy:", df['Ward'].unique())
ward_data = df[df['Ward'] == selected_ward].iloc[0]

col_a, col_b = st.columns(2)

with col_a:
    st.write(f"**Current Status for Ward {selected_ward}:**")
    st.write(f"* Heat Vulnerability: {ward_data['Vulnerability_Index']:.1f}/100")
    st.write(f"* Greenery Level (NDVI): {ward_data['Vegetation_Index_NDVI']}")

with col_b:
    st.write("**AI Recommended Actions:**")
    if ward_data['Vulnerability_Index'] > 70:
        st.warning("🚨 HIGH PRIORITY: Implement Cool Roof policies and rapid urban afforestation.")
    elif ward_data['Vulnerability_Index'] > 40:
        st.info("⚠️ MODERATE: Increase street-side tree canopy and preserve existing parks.")
    else:
        st.success("✅ LOW RISK: Maintain current green cover and monitor building density.")
