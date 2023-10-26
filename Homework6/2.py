from tkinter import *
from tkinter import ttk

def calculate(*args):
	try:
		I = float(mass.get()) / (float(height.get()) ** 2)
		IMT.set(round(I, 2))

		if I <= 16:
			result.set('Выраженный дефицит массы тела')
		elif 16 < I <= 18.5:
			result.set('Недостаточная масса тела')
		elif 18.5 < I <= 25:
			result.set('Норма')
		elif 25 < I <= 30:
			result.set('Избыточная масса тела')
		elif 30 < I <= 35:
			result.set('Ожирение 1 степени')
		elif 35 < I <= 40:
			result.set('Ожирение 2 степени')
		elif I > 40:
			result.set('Ожирение 3 степени')

	except Exception as e:
		IMT.set('Ошибка во вводе данных!')
	

root = Tk()
root.title('Индекс массы тела')
root.geometry('600x280')

mass = StringVar() 
height = StringVar() 
IMT = StringVar()
result = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Введите массу тела в килограммах: ', font=('Montserrat 15 bold'))
mass = ttk.Entry(mainframe, justify='center', width='96', textvariable=mass)

ttk.Label(mainframe, text='Введите рост в метрах: ', font=('Montserrat 15 bold'))
height = ttk.Entry(mainframe, justify='center', width='96', textvariable=height)

ttk.Button(mainframe, text='Посчитать!', width='50', command=calculate)
ttk.Label(mainframe, textvariable=IMT, font=('Montserrat 20 bold'))
ttk.Label(mainframe, textvariable=result, font=('Montserrat 20 bold'))

for child in mainframe.winfo_children(): 
	child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)
mass.focus()

root.mainloop()