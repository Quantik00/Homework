from tkinter import *
from tkinter import ttk

def calculate(*args):
	try:
		s_color = color.get()
		canvas.itemconfig(rec, fill=s_color)
		R = int(s_color[1:3], 16)
		G = int(s_color[3:5], 16)
		B = int(s_color[5:], 16)

		compl_R = str(hex(255 - R))[2:].upper()
		compl_G = str(hex(255 - G))[2:].upper()
		compl_B = str(hex(255 - B))[2:].upper()

		if compl_R == '0': compl_R = '00'
		if compl_G == '0': compl_G = '00'
		if compl_B == '0': compl_B = '00'
		
		s_compl_color = f'#{compl_R}{compl_G}{compl_B}'
		canvas.itemconfig(compl_rec, fill=s_compl_color)
		compl_color.set(s_compl_color)


	except Exception as e:
		compl_color.set('Ошибка во вводе данных!')
	

root = Tk()
root.title('Комплементарный цвет')
root.geometry('600x350')

color = StringVar()
compl_color = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text='Введите цвет в hex: ', font=('Montserrat 20 bold'))
entry = ttk.Entry(mainframe, justify='center', width='70', textvariable=color)
ttk.Button(mainframe, text='Вывести комплементарный цвет', width='50', command=calculate)

canvas = Canvas(mainframe, width=600, height=100)
ttk.Label(root, textvariable=color, font=('Montserrat 20 bold')).place(x=95,y=230)
rec = canvas.create_rectangle(60, 20, 60 + 180, 20 + 100, outline='')

ttk.Label(root, textvariable=compl_color, font=('Montserrat 20 bold')).place(x=385,y=230)
compl_rec = canvas.create_rectangle(350, 20, 350 + 180, 20 + 100, outline='')

for child in mainframe.winfo_children(): 
	child.grid_configure(padx=0, pady=5)

root.bind('<Return>', calculate)
entry.focus()

root.mainloop()