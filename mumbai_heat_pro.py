import requests
import pandas as pd
from tabulate import tabulate

def get_live_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=19.0760&longitude=72.8777&current_weather=true"
    try:
        res = requests.get(url).json()
        return res['current_weather']['temperature']
    except:
        return 30.0  # Fallback temp

def run_pro_app():
    df = pd.read_csv('mumbai_heat_base.csv')
    live_temp = get_live_weather()
    
    while True:
        print("\n" + "="*60)
        print(f"   MUMBAI HEATPULSE PRO | CURRENT CITY TEMP: {live_temp}°C")
        print("="*60)
        
        cmd = input("\nEnter Ward (e.g. G/N), 'ALL' for table, or 'EXIT': ").strip().upper()
        
        if cmd == 'EXIT': break
        
        if cmd == 'ALL':
            # Display everything in a clean table
            print("\n" + tabulate(df.head(10), headers='keys', tablefmt='psql', showindex=False))
        
        elif cmd in df['Ward'].values:
            ward_data = df[df['Ward'] == cmd].iloc[0]
            surface_temp = ward_data['Surface_Temp_Celsius']
            
            # Formatting the specific ward report
            report = [
                ["Ward Name", cmd],
                ["Surface Temp", f"{surface_temp:.2f}°C"],
                ["Greenery (NDVI)", f"{ward_data['Vegetation_Index_NDVI']:.2f}"],
                ["Heat Impact", "HIGH" if surface_temp > 38 else "MODERATE"]
            ]
            print("\n" + tabulate(report, tablefmt="fancy_grid"))
        else:
            print("Unknown command or Ward. Please try again.")

if __name__ == "__main__":
    run_pro_app()