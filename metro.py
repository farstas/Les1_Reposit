import csv
from datetime import datetime, timedelta, date
list_station = list()
dict_repairs = dict()

with open('metro_2017_09_06.csv', 'r', encoding = 'utf-8') as f:
    reader = csv.DictReader(f, delimiter = ';')
    for row in reader:
        list_station.append(row)

time_now = datetime.now() - timedelta(days = 60)



for station in list_station:
    repair = station['Ремонт эскалаторов']
    station = station['Станция метрополитена']
    if repair is not '':
        repair = repair.replace('-', ' ')
        repair = repair.split()
        repair[0] = datetime.strptime(repair[0], '%d.%m.%Y')
        repair[1] = datetime.strptime(repair[1], '%d.%m.%Y')
        if (time_now > repair[0]) and (time_now < repair[1]):
            dt_end = repair[1]
            dt_end = datetime.strftime(dt_end, '%d %B %Y')
            print ('Ремонтные работы ведутся на станции {}, дата окончания работ {}'.format(station, dt_end))
            dict_repairs[station] = repair
        


if dict_repairs == {}:
    print('Ремонтные работы не ведутся')
    


