import requests

def get_mumbai_weather():
    # Coordinates for Mumbai (approx. center)
    lat = 19.0760
    lon = 72.8777
    
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    print("Connecting to Mumbai Weather Satellite...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current = data['current_weather']
        
        print("\n--- LIVE MUMBAI DATA ---")
        print(f"Current Temp : {current['temperature']}°C")
        print(f"Wind Speed   : {current['windspeed']} km/h")
        print(f"Time Updated : {current['time']}")
    else:
        print("Failed to reach the satellite. Check your internet!")

get_mumbai_weather()