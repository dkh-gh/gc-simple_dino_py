# compile 2 exe!
# ДЗ: 
# 	x. заставить кактусы двигаться
# 	x. при коллизии закрасить игрока красным
# 	x. при выходе кактуса за левый край экана - перекинуть его за правый и изменить размер (случ. 1..3)
# 	x. реализовать прыжок
# 	x. правильная коллизия
#   x. счётчик
#   получше изучить декартову систему к.

import tkinter as tk
from time import sleep
from random import randint

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
	'jump_min_y': 50,
	'jump': False,
	'jump_direction': True, # True = up, False = down
}

collision = False

speed = 7
score = 5
cactus_1 = {
	'x': 400,
	'size': 1,
}
cactus_2 = {
	'x': 700,
	'size': 2,
}
cactus_3 = {
	'x': 1000,
	'size': 3,
}

def player_jump(event):
	global player, collision
	collision = False
	if event.keysym == 'space':
		if not player['jump']:
			player['jump'] = True
			# player['y'] = player['base_y']
			player['jump_direction'] = True

win.bind('<KeyPress>', player_jump)

while 1:
	# очистка
	img.delete('all')

	# изменение переменных
	cactus_1['x'] -= int(speed)
	cactus_2['x'] -= int(speed)
	cactus_3['x'] -= int(speed)

	speed = speed + (50-speed)/1000

	# логика 
	# прыжок
	if player['jump']:
		if player['jump_direction']:
			player['y'] = (player['y']*5+player['jump_min_y'])/6
			if player['y'] <= player['jump_min_y']+10:
				player['jump_direction'] = False
		else:
			player['y'] += ((player['y']*5+player['jump_min_y'])/6 - player['jump_min_y'])/3
			if player['y'] >= player['base_y']:
				player['y'] = player['base_y']
				player['jump'] = False

	# переброс кактусов
	if cactus_1['x'] < -10*cactus_1['size']:
		cactus_1['size'] = randint(1,3)
		cactus_1['x'] = 800+20*int(speed)
		# speed += 1
		score += 1
	if cactus_2['x'] < -10*cactus_2['size']:
		cactus_2['size'] = randint(1,3)
		cactus_2['x'] = 800+20*int(speed)
		# speed += 1
		score += 1
	if cactus_3['x'] < -10*cactus_3['size']:
		cactus_3['size'] = randint(1,3)
		cactus_3['x'] = 800+20*int(speed)
		# speed += 1
		score += 1

	# коллизия
	if collision:
		score -= 1
		collision = False
	if   player['x']+25 > cactus_1['x']-10*cactus_1['size'] \
	 and player['x']-25 < cactus_1['x']+10*cactus_1['size'] \
	 and player['y']+50 > 175 \
	 and player['y']-50 < 250:
		collision = True
	if   player['x']+25 > cactus_2['x']-10*cactus_2['size'] \
	 and player['x']-25 < cactus_2['x']+10*cactus_2['size'] \
	 and player['y']+50 > 175 \
	 and player['y']-50 < 250:
		collision = True
	if   player['x']+25 > cactus_3['x']-10*cactus_3['size'] \
	 and player['x']-25 < cactus_3['x']+10*cactus_3['size'] \
	 and player['y']+50 > 175 \
	 and player['y']-50 < 250:
		collision = True

	# if collision:
	# 	exit()

	# отрисовка
	win.title(f'{int(speed)} {score}')
	# ground
	img.create_line(0,250, 800,250)
	# player
	if not collision:
		img.create_rectangle(
			player['x']-25,player['y']-50,
			player['x']+25,player['y']+50,)
	else:
		img.create_rectangle(
			player['x']-25,player['y']-50,
			player['x']+25,player['y']+50, fill='red')
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

	# обновление отрисовки
	img.update()
	sleep(0.05)


