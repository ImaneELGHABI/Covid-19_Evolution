#Importing necessary libraries
import sqlite3 as sql
import pandas as pd
#The <connect> method allows us to create the database.
connexion=sql.connect('covid_19.db')
#The <connection.cursor()> method intended to temporarily memorize the data being processed, before their final transfer to the database.
cur=connexion.cursor()
#cur.execute('DROP TABLE Region')
#cur.execute('DROP TABLE daily')

#The following command allows us to create the table in which we will insert our data.
cur.execute('CREATE TABLE IF NOT EXISTS daily(ID INTEGER PRIMARY KEY AUTOINCREMENT,Date DATE,New_cases INTEGER,New_recoveries INTEGER, New_deaths INTEGER)')
cur.execute('CREATE TABLE IF NOT EXISTS Region(Region TEXT PRIMARY KEY,Total_cases INTEGER,Active_cases INTEGER,Total_deaths INTEGER,Total_recovered INTEGER)')

#Importing data
data_covid=pd.read_csv("https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/MA-times_series.csv")
region=pd.read_csv("https://raw.githubusercontent.com/aboullaite/Covid19-MA/master/stats/regions.csv")
#By the following lines we rename some columns of the data that we are going to use them
region.rename( columns={"Region / الجهة": "Region" }, inplace=True)
region.rename( columns={"Total Cases / إجمالي الحالات": "Total_cases" }, inplace=True)
region.rename( columns={"Active Cases / الحالات النشطة": "Active_cases" }, inplace=True)
region.rename( columns={"Total Deaths / إجمالي الوفيات": "Total_deaths" }, inplace=True)
region.rename( columns={"Total Recovered / إجمالي المعافين": "Total_recovered" }, inplace=True)
##
data_covid.rename( columns={"Dates/التواريخ": "Date" }, inplace=True)
data_covid.rename( columns={"Cases/الحالات": "New_cases" }, inplace=True)
data_covid.rename( columns={"Recovered/تعافى": "New_recoveries" }, inplace=True)
data_covid.rename( columns={"Deaths/الوفيات": "New_deaths" }, inplace=True)
#In this step, the <to_sql> method is used to convert the region data into the already created Region table.
#You should execute the following commented line only once
#region.to_sql('Region', connexion, if_exists='append', index=False )
#transfer to the database is triggered by the commit() method
connexion.commit()
#The <to_sql> method in this case converts daily data into a table already created Daily.
data_covid.to_sql('daily', connexion, if_exists='append', index=False )

connexion.commit()
#To ensure that our code works well, we used the following commands:
for item in cur.execute("SELECT Region FROM Region ORDER BY Total_deaths DESC"):
    print(item)

#for item in cur.execute("SELECT Region,Total_cases FROM Region where Total_cases=(SELECT Max(Total_cases)from Region)"):
 #   print(item)

#for item in cur.execute("SELECT * FROM Region where Region='Tanger-Tétouan-Al Hoceima'"):
#    print(item)
