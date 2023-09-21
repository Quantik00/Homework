with open('input10.txt') as f:
	words = f.read().split()

vowels = ['о', 'ё', 'у', 'ю', 'а', 'я', 'е', 'э', 'и', 'ы']

for word in words:
	new_word = word[0]
	for i in range(1, len(word)):
		new_word += word[i]
		if word[i] in vowels and word[i - 1] not in vowels:
			new_word += 'с' + word[i]
	print(new_word)