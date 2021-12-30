from Display import *
import sys
import time

game_state = False
button_clicked = False
button = Button()

while True:
	clock.tick(60)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	background(game_state)
	if button.draw(game_state):
		game_state = True

	pygame.display.update()