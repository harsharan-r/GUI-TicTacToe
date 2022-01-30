from GameLogic import *
import sys
import time

#setting game and menu variables
game_state = False
score = [0,0]

#intializing instances for game logic and menu button logic
Start_Text = 'Start Game'
Start_Game_Button = Button([600,200],[width/2,height/2],Start_Text,100,20)
game = Game(score)

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
	if not game_state:	
		if Start_Game_Button.draw():
			game_state = True

	if game_state:

		update_value = game.update()

		if update_value == 1:
			Start_Game_Button.clicked = False
			game_state = False
			game = Game([0,0])

		elif update_value == 2:

			game = Game(game.score)





	pygame.display.update()