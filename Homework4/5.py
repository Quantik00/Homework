import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

csv = pd.read_csv('BTC_data.csv')

dates = []
prices = []

for line in csv['time']:
	dates.append(line.split('T')[0])

for line in csv['close']:
	prices.append(int(line))



plt.figure(figsize=(10,6), dpi=150)
plt.plot(dates, prices, label='Зависимость цены BTC от времени')
plt.xticks(dates[::75], rotation=30)

degree = 3 
coefficients = np.polyfit(np.arange(len(prices)), prices, degree)
poly = np.poly1d(coefficients)

x = np.arange(len(prices))
plt.plot(dates, poly(x), label=f'Аппроксимация {degree}-й степени', linestyle='--')

plt.grid()
plt.title('График зависимости цены BTC от времени', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
plt.legend()

plt.show()