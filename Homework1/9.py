with open('input9.txt') as f:
	s = f.read()

counter = 0
for char in s:
	if 'A' <= char <= 'Z':
		counter += 1

print(counter)
