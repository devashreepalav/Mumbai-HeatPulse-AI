import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA
df = pd.read_csv('mumbai_heat_base.csv')

# 2. SET THE STYLE
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 3. CREATE A SCATTER PLOT
# X-axis: Vegetation (NDVI), Y-axis: Temperature
plot = sns.scatterplot(
    data=df, 
    x='Vegetation_Index_NDVI', 
    y='Surface_Temp_Celsius', 
    hue='Avg_Income_Level', # Color code by income
    size='Building_Density_Score', # Larger dots = more concrete
    sizes=(50, 400),
    palette='viridis'
)

# 4. ANNOTATE THE WARDS
# This helps us identify exactly which ward is the hottest/coolest
for i in range(df.shape[0]):
    plt.text(
        df.Vegetation_Index_NDVI[i]+0.005, 
        df.Surface_Temp_Celsius[i], 
        df.Ward[i], 
        fontsize=9
    )

plt.title("Mumbai Heat Analysis: Vegetation vs. Temperature per Ward")
plt.xlabel("Greenery Index (NDVI)")
plt.ylabel("Surface Temp (°C)")
plt.show()