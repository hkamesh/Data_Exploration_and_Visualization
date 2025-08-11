import pandas as pd
import numpy as np
import folium

np.random.seed(42)
num_points = 100
latitude = np.random.uniform(37.5, 38.5, num_points)
longitude = np.random.uniform(-123, -121, num_points)
value = np.random.randint(1, 100, num_points)

df = pd.DataFrame({
    'Latitude': latitude,
    'Longitude': longitude,
    'Value': value
})

df.to_csv('map_data.csv', index=False)
df = pd.read_csv('map_data.csv')
base_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)
for index, row in df.iterrows():
    popup_text = f"Value: {row['Value']}"
    folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(base_map)
base_map.save('interactive_map.html')
df = pd.read_csv('map_data.csv')
print("Basic Statistics:")
print(df.describe())

base_map = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=10)

for index, row in df.iterrows():
    popup_text = f"Value: {row['Value']}"
    folium.Marker([row['Latitude'], row['Longitude']], popup=popup_text).add_to(base_map)

base_map
