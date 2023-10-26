from tkinter import *
from tkinter import ttk

def calculate(*args):
	try:
		result.set(eval(inp.get()))
	except Exception as e:
		result.set('Ошибка во вводе данных!')
	

root = Tk()
root.title('Calculator')
root.geometry('600x200')

inp = StringVar() 
result = StringVar()

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

entry = ttk.Entry(mainframe, justify='center', width='96', textvariable=inp)
ttk.Button(mainframe, text='Посчитать!', width='50', command=calculate)
ttk.Label(mainframe, textvariable=result, font=('Montserrat 20 bold'))

for child in mainframe.winfo_children(): 
	child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)
entry.focus()

root.mainloop()