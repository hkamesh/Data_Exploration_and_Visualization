import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

world_data = pd.DataFrame({
    'Country': ['USA', 'Canada', 'India', 'Brazil', 'China'],
    'Value': [100, 150, 200, 80, 120]
})
india_states_data = pd.DataFrame({
    'State': ['Maharashtra', 'Karnataka', 'Tamil Nadu', 'Uttar Pradesh', 'Gujarat'],
    'Value': [50, 75, 60, 40, 30]
})
india_districts_data = pd.DataFrame({
    'District': ['Mumbai', 'Bengaluru', 'Chennai', 'Lucknow', 'Ahmedabad'],
    'Value': [20, 30, 25, 15, 10]
})

world_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
india_states_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
india_districts_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

world_data_geo = world_map.merge(world_data, how='left', left_on='name', right_on='Country')
india_states_data_geo = india_states_map.merge(india_states_data, how='left', left_on='name', right_on='State')
india_districts_data_geo = india_districts_map.merge(india_districts_data, how='left', left_on='name', right_on='District')

fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].set_title('World Data')
world_data_geo.boundary.plot(ax=axs[0])
world_data_geo.plot(column='Value', ax=axs[0], legend=True, legend_kwds={'label': "Values by Country"})

axs[1].set_title('India States Data')
india_states_data_geo.boundary.plot(ax=axs[1])
india_states_data_geo.plot(column='Value', ax=axs[1], legend=True, legend_kwds={'label': "Values by State"})

axs[2].set_title('India Districts Data')
india_districts_data_geo.boundary.plot(ax=axs[2])
india_districts_data_geo.plot(column='Value', ax=axs[2], legend=True, legend_kwds={'label': "Values by District"})

plt.tight_layout()
plt.show()
