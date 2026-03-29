import pandas as pd

df = pd.read_csv('mumbai_heat_base.csv')

def run_expert_system():
    while True: # This starts the loop
        print("\n" + "="*40)
        print("   MUMBAI HEATPULSE: LIVE ANALYZER   ")
        print("="*40)
        
        target = input("\nEnter Ward (or type 'EXIT' to quit): ").strip().upper()
        
        if target == 'EXIT':
            print("Closing HeatPulse. Stay cool, Mumbai!")
            break # This stops the loop
            
        ward_info = df[df['Ward'] == target]
        
        if not ward_info.empty:
            temp = ward_info['Surface_Temp_Celsius'].values[0]
            print(f"\n>>> Ward {target} Analysis <<<")
            print(f"Predicted Temp: {temp:.2f}°C")
            
            # Advice logic
            if temp > 38:
                print("ADVICE: Critical. Deploy mist-cooling fans.")
            else:
                print("ADVICE: Normal. Monitor humidity levels.")
        else:
            print("Ward not found. Try 'G/N', 'A', or 'K/W'.")

run_expert_system()