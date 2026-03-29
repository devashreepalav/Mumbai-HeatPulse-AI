import pandas as pd
import numpy as np

# 1. DEFINE THE WARDS
# Mumbai is split into 24 administrative wards.
wards = [
    'A', 'B', 'C', 'D', 'E', 'F/N', 'F/S', 'G/N', 'G/S', 
    'H/E', 'H/W', 'K/E', 'K/W', 'L', 'M/E', 'M/W', 'N', 
    'P/N', 'P/S', 'R/C', 'R/N', 'R/S', 'S', 'T'
]

# 2. CREATE THE DATASET
# We are simulating 'Ward-level' metrics which we will later replace with real satellite data.
data = {
    'Ward': wards,
    'Vegetation_Index_NDVI': np.random.uniform(0.1, 0.4, 24), # 0.1=Dry/Concrete, 0.4=Lush/Trees
    'Building_Density_Score': np.random.uniform(50, 95, 24),   # % of ward covered by buildings
    'Avg_Income_Level': np.random.choice(['Low', 'Medium', 'High'], 24)
}

df = pd.DataFrame(data)

# 3. ADD THE 'HEAT' LOGIC (The Science)
# Physics: Temp increases with Density and decreases with Vegetation.
df['Surface_Temp_Celsius'] = 32 + (df['Building_Density_Score'] * 0.1) - (df['Vegetation_Index_NDVI'] * 10)

print("--- Mumbai Ward Heat Analysis Initialized ---")
print(df.head())

# Save this for our Dashboard later
df.to_csv('mumbai_heat_base.csv', index=False)