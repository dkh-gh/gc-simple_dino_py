# compile 2 exe!

import tkinter as tk
from time import sleep

win = tk.Tk()
win.title('dino game')
img = tk.Canvas(
	win,
	width=800,
	height=300
)
img.pack()

player = {
	'x': 100,
	'y': 200,
	'base_y': 200,
	'jump_height': 100,
	'jump': False,
	'jump_direction': True,
}

speed = 3
cactus_1 = {
	'x': 400,
	'size': 1,
}
cactus_2 = {
	'x': 500,
	'size': 2,
}
cactus_3 = {
	'x': 600,
	'size': 3,
}

while 1:
	img.delete('all')

	cactus_1['x'] -= speed
	cactus_2['x'] -= speed
	cactus_3['x'] -= speed

	# ground
	img.create_line(0,250, 800,250)
	# player
	img.create_rectangle(
		player['x']-25,player['y']-50,
		player['x']+25,player['y']+50,)
	# cacrus 1
	img.create_rectangle(
		cactus_1['x']-10*cactus_1['size'],175,
		cactus_1['x']+10*cactus_1['size'],250,)
	# cacrus 2
	img.create_rectangle(
		cactus_2['x']-10*cactus_2['size'],175,
		cactus_2['x']+10*cactus_2['size'],250,)
	# cacrus 3
	img.create_rectangle(
		cactus_3['x']-10*cactus_3['size'],175,
		cactus_3['x']+10*cactus_3['size'],250,)


	sleep(0.05)
	img.update()


