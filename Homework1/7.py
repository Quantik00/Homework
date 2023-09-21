lst = [int(x) for x in input().split()]

num = -1
max_count = 0

for x in lst:
	count = lst.count(x)
	if count > max_count:
		max_count = count
		num = x

print(num)