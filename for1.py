school_list = [{'school_class' : '4a', 'scores': [3,4,4,5,2]}, {'school_class' : '4б', 'scores': [3,5,5,4,5,4,5]}]

scores_4a = school_list[0]['scores']
summ_scores_4a = 0
for stud in scores_4a:
	summ_scores_4a += int(stud)

scores_4b = school_list[1]['scores']
summ_scores_4b = 0
for stud in scores_4b:
	summ_scores_4b += int(stud)

summ_scores = summ_scores_4b + summ_scores_4a
avr_score = summ_scores / (len(scores_4a) + len(scores_4b))
avr_score_4a = summ_scores_4a / (len(scores_4a))
avr_score_4b = summ_scores_4b / (len(scores_4b))

print('Средний бал по школе = {}'.format(round(avr_score, 1)))
print('Средний бал по 4А = {}'.format(round(avr_score_4a, 1)))
print('Средний бал по 4Б = {}'.format(round(avr_score_4b, 1)))
