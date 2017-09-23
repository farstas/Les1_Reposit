def calculator_bot(bot, update, args):
    text= update.message.text
    text = text.replace('+', ' + ')
    text = text.replace('-', ' - ')
    text = text.replace('*', ' * ')
    text = text.replace('/', ' / ')
    user_text = text.split()
    user_text = user_text[2:]
    print(user_text)
    for items in user_text:
            if items == '*':
                index = user_text.index(items)
                user_text[index] = int(user_text[index - 1]) * int(user_text[index + 1])
                user_text[index - 1] = '?'
                user_text[index + 1] = '?'
                print(user_text)
    
    for items in user_text:
            if items == '/':
                index = user_text.index(items)
                user_text[index] = int(user_text[index - 1]) / int(user_text[index + 1])
                del user_text[index - 1]
                del user_text[index]
                print(user_text[index])


logging.info(text)
