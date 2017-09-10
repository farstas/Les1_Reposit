school_list = [{'school_class' : '4a', 'scores': [3,4,4,5,2]}, {'school_class' : '4б', 'scores': [3,5,5,4,5,4,5]}]
summ_scores = 0
line = 0

for cls in school_list: 
	summ_scores += sum(cls['scores'])
	line += len(cls['scores'])

avr_score = summ_scores / line

print('Средний бал по школе = {}'.format(round(avr_score, 1)))

summ_scores = 0
line = 0

for cls in school_list: 
	summ_scores = sum(cls['scores'])
	line = len(cls['scores'])
	name = cls['school_class']
	avr_score = summ_scores / line
	print('Средняя оценка по классу {} равна {}'.format(name, round(avr_score, 1)))
