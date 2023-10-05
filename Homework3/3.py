def nod(m, n):
	return m if n == 0 else nod(n, m % n)

a, b = map(int, input().split())

d = nod(a, b)
mx, my = None, None
minsum = 1e9

for x in range(-500, 500):
	for y in range(-500, 500):
		if a * x + b * y == d and abs(x) + abs(y) < minsum:
			minsum = abs(x) + abs(y)
			mx = x
			my = y

print(mx, my, d)