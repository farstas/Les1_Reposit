namelist = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']
name = input('Введите имя для поиска: ')

while namelist:
	name = namelist.pop()
	if name == 'Валера':
		print('Валера нашелся')
		break
else:
	print('Валеры в списке нет')

