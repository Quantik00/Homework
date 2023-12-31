from random import randint
from tkinter import *

WIDTH = 300
HEIGHT = 200

colors = ['green', 'red', 'blue', 'black', 'yellow']


class Ball:
	def __init__(self, color='green'):
		# храним размер, при каждом создании объекта будет выбираться случайно
		self.R = randint(10, 50)
		self.x = randint(self.R, WIDTH - self.R)  # храним положение по x и y
		self.y = randint(self.R, HEIGHT - self.R)
		# это по сути шаг движения шаров. если увеличить -- будут двигаться быстрее
		self.dx, self.dy = (10, 10)
		self.ball_id = canvas.create_oval(self.x - self.R,
										  self.y - self.R,
										  self.x + self.R,
										  self.y + self.R, fill=color)  # при создании шарика отрисовываем его

	def move(self):
		self.x += self.dx
		self.y += self.dy
		if self.x + self.R > WIDTH or self.x - self.R <= 0:  # отражение от стенок
			self.dx = -self.dx
		if self.y + self.R > HEIGHT or self.y - self.R <= 0:  # отр
			self.dy = -self.dy

	def show(self):
		canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
	rnd = randint(0, len(colors) - 1)
	balls.append(Ball(colors[rnd]))

	# здесь мы уже привычно обращаемся к balls как к глобальной переменной. На самом деле дело в том, что нам лень писать классы.


def tick():
	for ball in balls:
		ball.move()
		ball.show()
	root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
# сделаем так, чтобы нажатие левой кнопки на поле выводило координаты точки, в которую мы нажали
canvas.bind('<Button-1>', click_handler)
balls = [Ball() for i in range(5)]
# делаем шаг перемещения и отрисовки шаров. поскольку mainloop циклит наше приложение, это будет происходить, пока мы не закроем окно
tick()
root.mainloop()
