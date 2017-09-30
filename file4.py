import csv
from geopy.distance import great_circle

list_station = list()
list_metro = list()
dict_metro = dict()

with open('metro_2017_09_06.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        list_metro.append(row)

with open('stations_2017_09_14.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        list_station.append(row)


for met in list_metro:
	metro = met['Станция метрополитена']
	met_geo = met['Геоданные']
	met_geo = met_geo.replace('{type=Point, coordinates=[', '')
	met_geo = met_geo.replace(',', '')
	met_geo = met_geo.replace(']', '')
	met_geo = met_geo.replace('}', '')
	met_geo = met_geo.split()
	met_lat = met_geo[0]
	met_long = met_geo[1]
	for st in list_station:
		station = st['StationName']
		st_geo = st['geoData']
		st_geo = st_geo.replace('{type=Point, coordinates=[', '')
		st_geo = st_geo.replace(',', '')
		st_geo = st_geo.replace(']', '')
		st_geo = st_geo.replace('}', '')
		st_geo = st_geo.split()
		st_lat = st_geo[0]
		st_long = st_geo[1]
		print(station)
		print(st_lat)
		print(st_long)
		break

