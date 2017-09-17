answer={'привет': 'И тебе привет!', 'как дела?': 'Лучше всех', 'пока': 'Увидимся'}

def get_answer(question):
		
		return answer.get(question)


if __name__ == '__main__':
	question=input('Введите привет, как дела? или пока: ').lower()
	print(get_answer(question))

