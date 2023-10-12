import numpy as np

l1 = list(np.random.randint(0, 200, 100))
l2 = list(np.random.randint(0, 200, 100))

print('Уникальные для первого списка: ')
for x in l1:
	if x not in l2: print(x, end=' ')
print()

print('Уникальные для второго списка: ')
for x in l2:
	if x not in l1: print(x, end=' ')
print()

print('Уникальные для объединения списков: ')
union = l1 + l2
for x in union:
	if union.count(x) == 1:
		print(x, end = ' ')
print()

print('Содержащиеся в обоих списках: ')
for x in l1:
	if x in l2: print(x, end=' ')
print()
