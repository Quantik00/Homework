import numpy as np

class segTree:
	def __init__(self, data: list):
		self.data = data
		self.build()

	def build(self) -> None:
		ln = len(self.data)
		lb = np.log2(ln)
		self.data = self.data
		if lb != int(lb):
			lb = int(lb) + 1
			for i in range(ln, 2 ** lb):
				self.data.append(0)

		self.tree = [0 for i in range(len(self.data) - 1)] + self.data
		self.calc_tree()

	def calc_tree(self):
		for i in range(len(self.tree) + 1, 2, -2):
			s1 = self.tree[i - 2]
			s2 = self.tree[i - 3]
			sm = s1 + s2
			self.tree[(i - 4) // 2] = sm

	def sum(self, l, r):
		def tree_sum(self, l: int, r: int, tl = 0, tr = len(self.data)-1):			
			root = self.tree[0]
			summ = 0
			
			tm = (tl + tr + 1) // 2
			if tr == tl:
				return self.data[tm]

			if l <= tl and r >= tr:
				
				index1 = (len(self.data) - 1) + tr
				index2 = (len(self.data) - 1) + tl + 1
				
				while index1 != index2:
					index1 = max((index1 - 2) // 2, 0)
					index2 = max((index2 - 2) // 2, 0)
				
				if tl + 1 == tr:
					return self.tree[(index1 - 2) // 2]
				else:
					return self.tree[index1]

			go_left = l < tm
			go_right = r >= tm
			
			if go_left: 
				summ += tree_sum(self, l, r, tl = tl, tr = tm - 1)
			if go_right:
				summ += tree_sum(self, l, r, tl = tm, tr = tr)
			
			return summ
		return tree_sum(self, l, r)


	def update(self, l, r, value):			
		for i in range(l, r + 1):
			self.data[i] += value
		self.build()


tree = segTree([5, 2, 3, 4, 5, 6, 7, 8, 9])
print(tree.data)

print(tree.sum(0, 7))

print(tree.tree)
print(tree.data)

tree.update(2, 3, 45)

print(tree.data)
print(tree.tree)