import csv
from answers import answer

with open('export.csv','w', encoding = 'utf-8', newline = '') as table:
	fields = ['вопрос', 'ответ']
	writer = csv.DictWriter(table,fields, delimiter = ';')
	writer.writeheader()

	for questions, Value in answer.items():
		writer.writerow({fields[0]:questions, fields[1]:Value})
		