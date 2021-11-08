# -*- coding: utf-8 -*-
"""#18 How many people live around you

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qeRS3Pekctphppod0-ewCzmclNtJimOP?usp=sharing

# **How many people live around you**

"""

pip install osmnx

import pandas as pd
import osmnx as ox
import numpy as np
import requests

# What is your address
address = 'Matyas 11, Budapest, Hungary'
country = 'HUN'
month = '2019-06'

# Find out the geoposition
lat, lon = ox.geocode(address)
print('Geoposition:', country, lat, lon)

# 1-km range coordinates
min_lat = lat - 30/3600
max_lat = lat + 30/3600
min_lon = lon - 30/3600
max_lon = lon + 30/3600
print('Coordinates:', min_lat, min_lon, max_lat, max_lon)

# target area map
ox.plot_figure_ground(point=(lat, lon), dist=1000)

# build url
aws_s3 = 'http://dataforgood-fb-data.s3.amazonaws.com/'
url = aws_s3 + 'csv/month=%s/country=%s/type=total_population/%s_total_population.csv.gz' % (month, country, country)
print(url)

# download file
r = requests.get(url, stream = True) 
with open(country + '.csv', 'wb') as file: 
	for block in r.iter_content(chunk_size = 1024):
		if block: 
			file.write(block)

# read to dataframe
df = pd.read_csv(country + '.csv', sep='\t', dtype='float32')
print(df.head())

# Calculate number of people
cond1 = df['latitude'] > min_lat
cond2 = df['latitude'] < max_lat
cond3 = df['longitude'] > min_lon
cond4 = df['longitude'] < max_lon
sum(df.loc[cond1 & cond2 & cond3 & cond4, 'population'])
