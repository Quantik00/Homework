def turnRight(dx, dy):
	if (dx, dy) == (1, 0):
		return (0, 1)
	elif (dx, dy) == (0, 1):
		return (-1, 0)
	elif (dx, dy) == (-1, 0):
		return (0, -1)
	else:
		return (1, 0)

n, m = map(int, input().split())

matrix = [None] * m
for i in range(m):
	matrix[i] = [0] * n

x = 0
y = 0
dx = 1
dy = 0

# заполняем контур
for i in range(1, n * m):
	if matrix[y][x] != 0: break

	matrix[y][x] = i
	
	if x + dx >= n or y + dy >= m or x + dx < 0:
		dx, dy = turnRight(dx, dy)

	x += dx
	y += dy


start = matrix[1][0]
x = 1
y = 1
dx = 1
dy = 0

# заполняем внутреннюю часть 
while start < n * m:
	if matrix[y + dy][x + dx] != 0: 
		dx, dy = turnRight(dx, dy)

	matrix[y][x] = start + 1

	x += dx
	y += dy

	start += 1

for y in range(m):
	for x in range(n):
		matrix[y][x] *= y + 1

for line in matrix:
	print(line)