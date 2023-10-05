size, symb = input().split()
size = int(size)

for i in range(size // 2 + size % 2):
	print(symb * (i + 1))

for i in range(size // 2, 0, -1):
	print(symb * i)