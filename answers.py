def get_answer(question):
		answer={'привет': 'И тебе привет!', 'как дела?': 'Лучше всех', 'пока': 'Увидимся'}
		return answer.get(question)

question=input('Введите привет, как дела? или пока: ')
print(get_answer(question))