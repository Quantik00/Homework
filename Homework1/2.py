lst = input().split()

n = int(lst[0])
s = lst[1]
s2 = ''

for i in range(n, len(s) + 1, n):
	group = s[i - n:i]
	s2 += group[::-1]

print(s2)