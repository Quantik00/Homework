import matplotlib.pyplot as plt

with open('data.csv') as f:
	count = []
	freq = []

	for t in f.read().splitlines():
		count.append(int(t.split(';')[0]))
		freq.append(float(t.split(';')[1]))

plt.figure(figsize=(10,6), dpi=100)
plt.bar(count, freq, label='График')
plt.xlabel('Число отсчетов')
plt.ylabel('Частота')
plt.grid()
plt.legend()
plt.title('Упражнение 1', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.show()