import csv
list_station = list()
dict_streets = dict()

with open('stations_2017_09_14.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        list_station.append(row)


for station in list_station:
    street = station['Street']
    station = station['StationName']
    if dict_streets.get(street) is None:
        dict_streets[street] = [station]
    else:
        dict_streets[street] += [station]


lane = 0
for st in dict_streets:
    if (len(dict_streets[st]) > lane) and (st != 'проезд без названия'):
        lane  = len(dict_streets[st])
        long_street = st

print('Улица - {}, количество остановок - {}'.format(long_street, len(dict_streets[long_street])))
print(dict_streets[long_street])



