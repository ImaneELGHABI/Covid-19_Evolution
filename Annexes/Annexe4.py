#Choropleth map of total deaths
#Importing necessary libraries
import os
import pandas as pd
import folium

#Importing the data
json = os.path.join('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/ma-convid19-state.geojson')
covid_reg=pd.read_csv('https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv')

#We used the following command to rename some columns
covid_reg.rename( columns={"Region / الجهة": "Region" }, inplace=True)
covid_reg.rename( columns={"Total Cases / إجمالي الحالات": "Total_cases" }, inplace=True)
covid_reg.rename( columns={"Active Cases / الحالات النشطة": "Active_cases" }, inplace=True)
covid_reg.rename( columns={"Total Deaths / إجمالي الوفيات": "Total_deaths" }, inplace=True)
covid_reg.rename( columns={"Total Recovered / إجمالي المعافين": "Total_recovered" }, inplace=True)

#The following line adds a column called 'ID'
covid_reg['ID']=[1,2,3,4,5,6,7,8,9,10,11,12]

#The <folium.Map> command creates the map object centered on the latitude "31.794525" and longitude "-7.0849336":
m = folium.Map(location=[31.794525 ,-7.0849336], zoom_start=5)

#<m.choropleth> allows us to plot our colored map
m.choropleth(geo_data=json, data=covid_reg, #First, we specify the data
columns=['ID','Total_deaths'], #The following columns are those we will use and belong to our 'data' dataframe.
key_on='properties.ID',# this column belongs to our json file 'geo_data', it contains the same data as the 'ID' column.
#so they are the common columns between the two data, which allowed us to link the two files.
color="Total_deaths",
fill_color='YlOrRd', fill_opacity=1, line_opacity=0.9,
legend_name='Total Deaths'
)

#The following commands allow us to control the style of our map.
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
fields=['Name-FR','Total Deaths'],
aliases=['Region: ','Total deaths:'],
style=("background-color: white; color: black; font-family: arial; font-size: 12px; padding: 10px;") )
)
m.add_child(sty)
m.keep_in_front(sty)
folium.LayerControl().add_to(m)

#With this last line, we saved our map in an existing html file.
m.save('index2.html')
