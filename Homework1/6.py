lst = [int(x) for x in input().split()]

for x in lst:
	if lst.count(x) == 1:
		print(x)