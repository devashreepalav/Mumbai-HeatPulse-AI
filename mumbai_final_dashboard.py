import requests
import pandas as pd

def get_live_temp():
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    try:
        data = requests.get(url).json()
        return data['current_weather']['temperature']
    except:
        return "Unknown"

def run_dashboard():
    df = pd.read_csv('mumbai_heat_base.csv')
    live_temp = get_live_temp()
    
    print("\n" + "="*50)
    print(f"   MUMBAI HEATPULSE DASHBOARD | LIVE: {live_temp}°C")
    print("="*50)
    
    while True:
        target = input("\nEnter Ward to analyze (or 'EXIT'): ").strip().upper()
        if target == 'EXIT': break
            
        ward_info = df[df['Ward'] == target]
        if not ward_info.empty:
            ward_temp = ward_info['Surface_Temp_Celsius'].values[0]
            diff = ward_temp - float(live_temp) if live_temp != "Unknown" else 0
            
            print(f"\nWARD {target} REPORT:")
            print(f"- Localized Surface Temp: {ward_temp:.2f}°C")
            print(f"- Variation from City Avg: {diff:+.2f}°C")
            
            if diff > 2:
                print(">>> WARNING: This ward is a severe Heat Island!")
        else:
            print("Invalid Ward. Try A, G/N, or K/E.")

run_dashboard()