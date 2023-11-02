from math import sqrt

def get_cos(v1, v2):
	return (v1 * v2) / (v1.get_length() * v2.get_length())

def get_sin(v1, v2):
	cos = get_cos(v1, v2)
	return sqrt(1 - cos ** 2)

def triangle_square(v1, v2):
	return v1.get_length() * v2.get_length() * get_sin(v1, v2) / 2

class Vector():
	def __init__(self, x, y, z):
		assert (type(x) == int or type(x) == float), 'Координаты должны быть числовыми'
		assert (type(y) == int or type(y) == float), 'Координаты должны быть числовыми'
		assert (type(z) == int or type(z) == float), 'Координаты должны быть числовыми'

		self.x = x
		self.y = y
		self.z = z

	def __add__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


	def __sub__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x - other.x, self.y - other.y, self.z - other.z)


	def __mul__(self, other):
		if isinstance(other, Vector):
			return self.x * other.x + self.y * other.y + self.z * other.z

		elif isinstance(other, int) or isinstance(other, float):
			return Vector(self.x * other, self.y * other, self.z * other)


	def __str__(self):
		return f'x = {self.x} y = {self.y} z = {self.z}'


	def get_mass_center(self):
		return f'x = {self.x / 2} y = {self.y / 2} z = {self.z / 2}'


	def get_length(self):
		return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

	
# Ex. 1.1
v1 = Vector(1, 1, 1)
v2 = Vector(2, 3, 4)
v3 = v1 - v2
print(v2.get_mass_center())

# Ex 1.2

points = [(1, 1, 1), (1, 2, 3), (4, 5, 6), (2, 5, 1), (7, 1, 1)]
max_square = 0
for i in range(len(points)):
	for j in range(i + 1, len(points)):
		for k in range(j + 1, len(points)):
			x1 = points[j][0] - points[i][0]
			y1 = points[j][1] - points[i][1]
			z1 = points[j][2] - points[i][2]

			x2 = points[k][0] - points[i][0]
			y2 = points[k][1] - points[i][1]
			z2 = points[k][2] - points[i][2]

			v1 = Vector(x1, y1, z1)
			v2 = Vector(x2, y2, z2)

			square = triangle_square(v1, v2)
			max_square = max(max_square, square)

print(max_square)