
# 🏙️ Mumbai HeatPulse: Strategic Urban Climate Intelligence

A comprehensive Geospatial AI dashboard designed to analyze and mitigate the **Urban Heat Island (UHI)** effect across Mumbai's administrative wards. This tool correlates real-time satellite vegetation data (NDVI) with surface temperatures to provide actionable cooling strategies.

https://mumbai-heatpulse-ai-spke67ghqrasb4pml7vzm4.streamlit.app/

## 🚀 Core Features
* **Interactive Vulnerability Map:** A geospatial visualization of Mumbai's wards, color-coded by a custom 'Heat Vulnerability Index' (0-100 scale).
* **Real-Time Satellite Integration:** Fetches live localized weather data for Mumbai via the Open-Meteo API.
* **Urban Forestry Simulator:** A "What-If" planning tool that allows users to simulate how increasing canopy cover (NDVI) reduces localized surface temperatures.
* **AI Strategic Advisor:** Generates ward-specific "Heat Action Plans" based on calculated risk levels, providing tailored mitigation advice.
* **Automated Data Rankings:** Identifies high-risk "Concrete Jungle" wards vs. climate-resilient forested wards.

## 🛠️ Tech Stack
* **Frontend/App Framework:** Streamlit
* **Data Visualization:** Plotly Express (Mapbox & Scatter Plots)
* **Data Processing:** Pandas, NumPy
* **API Integration:** Requests (Open-Meteo API)
* **Deployment:** GitHub & Streamlit Community Cloud

## 📊 Technical Methodology
The app utilizes a weighted multi-criteria analysis to determine the **Vulnerability Index**:
- **Temperature (50%)**: Land Surface Temperature data.
- **Building Density (30%)**: Infrastructure density metrics.
- **NDVI (20%)**: Normalized Difference Vegetation Index (Greenery cover).

## 📈 Impact
Our analysis identifies that wards with **NDVI below 0.15** show significantly higher average temperatures compared to forested wards (like R/C), highlighting critical areas for Miyawaki forest interventions.

---
Developed with ❤️ for a cooler Mumbai.
