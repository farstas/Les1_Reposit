namelist = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
	while namelist:
		name1 = namelist.pop()
		if name1 == name:
			print('{} нашелся'.format(name))
			return
	print('{} в списке нет'.format(name))

find_person('Саша')
