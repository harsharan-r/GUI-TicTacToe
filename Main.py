from GameLogic import *
import sys
import time

#setting game and menu variables
game_state = False
button_clicked = False

#intializing instances for game logic and menu button logic
button = Button()
game = Game()

#adding window name
pygame.display.set_caption("Tic Tac Toe")

#setting framerate 
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