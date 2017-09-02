
def get_summ(one, two, delimeter=' '):
	return str(one) + str(delimeter) + str(two)

one=input('Введите аргумент 1: ')
two=input('Введите аргумент 2: ')
delimeter=input('При необходимости введите аргумент 3: ')
print(get_summ(one, two, delimeter).upper())