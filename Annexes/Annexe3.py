#Choropleth map of total recoveries#

#Import necessary libraries
import os
import pandas as pd
import folium

#Import data
json = os.path.join('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/ma-convid19-state.geojson')
covid_reg=pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv')

#Rename some columns
covid_reg.rename(columns={"Region / الجهة": "Region"}, inplace=True)
covid_reg.rename(columns={"Total Cases / إجمالي الحالات": "Total_cases"}, inplace=True)
covid_reg.rename(columns={"Active Cases / الحالات النشطة": "Active_cases"}, inplace=True)
covid_reg.rename(columns={"Total Deaths / إجمالي الوفيات": "Total_deaths"}, inplace=True)
covid_reg.rename(columns={"Total Recovered / إجمالي المعافين": "Total_recovered"}, inplace=True)

#Add a new column named 'ID'
covid_reg['ID']=[1,2,3,4,5,6,7,8,9,10,11,12]

#Create the map object centered on the point of latitude "31.794525" and longitude "-7.0849336"
m = folium.Map(location=[31.794525,-7.0849336], zoom_start=5)

#Create the colored choropleth map
m.choropleth(geo_data=json, data=covid_reg, #First specify the data
columns=['ID','Total_recovered'], #The following columns belong to our 'data' dataframe
key_on='properties.ID', #This column belongs to our 'geo_data' json file, it contains the same data as the 'ID' column.
#Therefore, these are the common columns between the two data, which allows us to link the two files.
color="Total_recovered",
fill_color='YlGn', fill_opacity=1, line_opacity=0.9,
legend_name='Total Recoveries'
)

#Control the style of the map
style_function = lambda x: {
'fillOpacity': 0.1,
'weight': 0.1}
highlight_function = lambda x: {'fillColor': 'red',
'fillOpacity': 0.50,
'weight': 0.1}
sty = folium.features.GeoJson(
json,
style_function=style_function,
control=False,
highlight_function=highlight_function,
tooltip=folium.features.GeoJsonTooltip(
fields=['Name-FR','Total Recovered'],
aliases=['Region: ','Total Recovered: '],
style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;")
)
)
m.add_child(sty)
m.keep_in_front(sty)
folium.LayerControl().add_to(m)

#Save the map to an html file
m.save('index1.html')
