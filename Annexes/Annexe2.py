##### Bubble Map of Confirmed Cases ####

# Necessary libraries
import folium
import pandas as pd
import os

# Importing data
covid_map = pd.read_excel(r'map_data.xlsx')
json = os.path.join('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/ma-convid19-state.geojson')

# Multiplying the 'Longitude' column by -1 because Excel doesn't allow negative values
covid_map["Longitude"] *= -1

# Creating the map object centered on latitude "31.794525" and longitude "-7.0849336"
morocco_map = folium.Map(location=[31.794525 ,-7.0849336], zoom_start=6, tiles='Stamen Terrain')

# <scale> allows us to control the scale of the bubbles
scale = 1000

for city in covid_map.index:
    # <loc> generates labels to read and write data
    lat = covid_map.loc[city]["Latitude"]
    lng = covid_map.loc[city]["Longitude"]
    confirmed = covid_map.loc[city]["Confirmed_cases"]
    
    # <CircleMarker()> method places a marker on the map at the coordinate point
    marker_confirmed = folium.CircleMarker(location=[lat, lng], radius=confirmed/scale,
                                          color="red", fill=True, popup="Total cases: %s" % confirmed,
                                          tooltip=covid_map.loc[city]['Region'])
    
    # Adding bubbles to the map
    marker_confirmed.add_to(morocco_map)

# Saving the map in an already created html file
morocco_map.save('map.html')

