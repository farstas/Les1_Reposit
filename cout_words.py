with open('referat.txt','r', encoding = 'utf - 8') as text:
	words = text.read()

print(words)
text_words = words.split()
print(len(text_words))