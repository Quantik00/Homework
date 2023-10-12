import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv('iris_data.csv')

species = set(csv['Species'])
percents = []

for specie in species:
	percents.append(list(csv['Species']).count(specie) / len(csv))

less_than_12 = 0
between_12_and_15 = 0
greater_than_15 = 0

for entry in csv['PetalLengthCm']:
	if entry < 1.2:
		less_than_12 += 1
	if 1.2 < entry < 1.5:
		between_12_and_15 += 1
	if entry > 1.5:
		greater_than_15 += 1

fig = plt.figure(figsize=(10, 6), dpi=100)

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.pie(percents, labels=species)
ax2.pie([less_than_12, between_12_and_15, greater_than_15], labels=[
		'Меньше 1.2 см.', 'Больше 1.2 см. и меньше 1.5 см', 'Больше 1.5 см.'])

plt.show()
