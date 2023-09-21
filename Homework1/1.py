lst = input.split()

# print(lst)

n = int(lst[0])

for i in range(1, n + 1):
	if str(i) not in lst[1:]:
		print(i)
		break