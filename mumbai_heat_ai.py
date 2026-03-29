import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. LOAD YOUR DATA
df = pd.read_csv('mumbai_heat_base.csv')

# 2. TRAIN THE AI (The "Learning" Phase)
# We want to predict 'Surface_Temp_Celsius' 
# based on 'Vegetation_Index_NDVI' and 'Building_Density_Score'
X = df[['Vegetation_Index_NDVI', 'Building_Density_Score']] 
y = df['Surface_Temp_Celsius']

model = LinearRegression()
model.fit(X, y)

print("--- AI Model Trained Successfully ---")

# 3. THE "WHAT IF" SCENARIO (Prediction)
# Imagine a new development project in a ward:
# Low greenery (0.1) and High density (90%)
new_site = [[0.1, 90]] 
prediction = model.predict(new_site)

print(f"Predicted Temperature for new development: {prediction[0]:.2f}°C")

# 4. SHOW THE IMPACT OF TREES
# What if we increase greenery to 0.4 at that same site?
greener_site = [[0.4, 90]]
better_prediction = model.predict(greener_site)

reduction = prediction[0] - better_prediction[0]
print(f"Predicted Temp with more trees: {better_prediction[0]:.2f}°C")
print(f"AI suggests trees would cool this area by: {reduction:.2f}°C")