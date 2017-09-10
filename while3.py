def ask_user():
	while True:
		user_say = input('Как дела? ').lower()
		if user_say == "хорошо":
			break

ask_user()
