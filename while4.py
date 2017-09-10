def get_answer(a):
		answer={'привет': 'И тебе привет!', 'как дела?': 'Лучше всех', 'пока': 'Увидимся'}
		result = answer.get(a)
		return result

def ask_user():
		while True:
			try:
				user_text=input('Введите привет, как дела? или пока: ').lower()
				print(get_answer(user_text))
				if user_text == "пока!":
					print('До новых встреч!')
			except KeyboardInterrupt:
				print( 'Даже не пытайся!')

ask_user()



