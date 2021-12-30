from GameLogic import *
import sys
import time

game_state = False
button_clicked = False
button = Button()

game = Game()

pygame.display.set_caption("Tic Tac Toe")

FPS = 60

while True:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	background(game_state)
	if button.draw(game_state):
		game_state = True

	if game_state:
		game.update()

	pygame.display.update()