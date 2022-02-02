from GameLogic import *
import sys
import time
import os

pygame.init()
pygame.mixer.init()

#setting game and menu variables
game_state = False
score = [0,0]
background_music = pygame.mixer.Sound(os.path.join("Assets","dj quads - its near.mp3"))

#intializing instances for game logic and menu button logic
Start_Text = 'Start Game'
Start_Game_Button = Button([600,200],[width/2,height/2],Start_Text,100,20)
game = Game(score)

#adding window name
pygame.display.set_caption("Tic Tac Toe")

#setting framerate 
FPS = 60

background_music.set_volume(0.1)
background_music.play(loops=-1)

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
	