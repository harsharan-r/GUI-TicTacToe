import pygame
from Display import *
import os


class Game:

	def __init__(self, score):

		self.place_sound = pygame.mixer.Sound(os.path.join("Assets","Piece_Sound.mp3"))
		#list of which board squares are occupied
		self.board = [0 for i in range(9)]

		#stores the value of the square you are hovering over
		self.selected_square = 0

		#empty square information
		sqr_pos = [0,270,540]
		sqr_height, sqr_width = 260, 260
		self.square_pos = [pygame.Rect(i,j,sqr_width,sqr_height) for i in sqr_pos for j in sqr_pos]

		#loading images of the 'X' and 'O'
		X_image = pygame.image.load(os.path.join('Assets','X.png'))
		O_image = pygame.image.load(os.path.join('Assets','O.png'))

		#scaling the images to the size of the empty squares
		self.X_Obj = pygame.transform.scale(X_image,(sqr_height,sqr_width))
		self.O_Obj = pygame.transform.scale(O_image,(sqr_height,sqr_width))

		#player one will be X and player 2 will be O
		self.player = 1
		self.current_piece = 'X'

		#gives status on if you have clicked a square to place a piece
		self.clicked = False

		#game status; nothing = 0, game won = 1 game draw = 2
		self.game_status = 0

		#menus
		self.main_menu_button = Button([250,100],[250,500],"Main Menu",50,5)
		self.replay_button = Button([250,100],[550,500],"Replay",50,5)
		self.draw_menu = Menu((600,400), (width/2,height/2), dark_red, "Its a Draw!", (width/2,350), auto_text_size=True)
		self.win_O_menu = Menu((600,400), (width/2,height/2), dark_red, "O Wins!", (width/2,350), auto_text_size=True)
		self.win_X_menu = Menu((600,400), (width/2,height/2), dark_red, "X Wins!", (width/2,350), auto_text_size=True)

		#labels
		score_font = pygame.font.SysFont('Poppins-Regular', 80)
		self.score_label = score_font.render(f"{score[0]} - {score[1]}",1,"#FEFFFA")
		self.score_label_rect = self.score_label.get_rect(midright=(725,750))
		self.score = score

	def draw(self):
		for idx, piece in enumerate(self.board):
			if piece == 'X':
				#print X onto respective squares 
				X_rect = self.X_Obj.get_rect(center = self.square_pos[idx].center)
				screen.blit(self.X_Obj, X_rect)

			elif piece == 'O':
				#print O onto respective square
				O_rect = self.O_Obj.get_rect(center = self.square_pos[idx].center)
				screen.blit(self.O_Obj, O_rect)

	def check_win(self):
		
		#column win detection
		for i in range(0,9,3):
			if len(set(self.board[i:i+3])) == 1 and set(self.board[i:i+3]) != {0}:
				return True
		
		#row win detection
		for i in range(0,3):
			if len(set(self.board[i:i+7:3])) == 1 and set(self.board[i:i+7:3]) != {0}:
				return True

		#diagonal
		if len(set(self.board[0:9:4])) == 1 and set(self.board[0:9:4]) != {0}:
			return True

		#opposite diagonal
		if len(set(self.board[2:7:2])) == 1 and set(self.board[2:7:2]) != {0}:
			return True

		return False

	def check_draw(self):

		for i in self.board:
			if i == 0:
				return False
		return True

	def mouse_hover(self):
		pos = pygame.mouse.get_pos()
		#goes through each square to check if the cursor is over it
		for i in range(len(self.square_pos)):

			#if the cursor is over a square
			if self.square_pos[i].collidepoint(pos) and self.board[i] == 0:

				#records the square your cursor is on
				self.selected_square = i

				#shows a preview of the piece in the square you are hovering over
				if self.player == 1:
					self.preview_X_rect = self.X_Obj.convert_alpha()
					self.preview_X_rect.set_alpha(128)
					X_rect = self.preview_X_rect.get_rect(center = self.square_pos[i].center)
					screen.blit(self.preview_X_rect, X_rect)

				else:
					self.preview_O_rect = self.O_Obj.convert_alpha()
					self.preview_O_rect.set_alpha(128)
					O_rect = self.preview_O_rect.get_rect(center = self.square_pos[i].center)
					screen.blit(self.preview_O_rect, O_rect)
		
	def update(self):

		if self.game_status == 0:	

			#changing current piece depending on whos turn it is
			self.current_piece = 'X' if self.player == 1 else 'O'

			#checks if you click a square
			if pygame.mouse.get_pressed()[0]:
				self.clicked = True

			else:
				#when you let go of the mouse button it will record the square you are over and place your piece on it
				if self.clicked:
					self.place_sound.play()
					if self.board[self.selected_square] == 0:
						self.board[self.selected_square] = self.current_piece
						self.player = 1 if self.player == 0 else 0
						self.clicked = False

			self.mouse_hover()

			if self.check_win():
				self.game_status = 1

			elif self.check_draw():
				#change with draw menu
				self.game_status = 2

			#updating graphics
			self.draw()

		elif self.game_status == 1:

			if self.player == 0:
				self.win_X_menu.draw()

			elif self.player == 1:
				self.win_O_menu.draw()
			
			if self.main_menu_button.draw():
				return 1

			if self.replay_button.draw():
				
				self.score[self.player] += 1
				return 2
			
		elif self.game_status == 2:
			
			self.draw_menu.draw()

			if self.main_menu_button.draw():
				return 1

			if self.replay_button.draw():

				return 2

		screen.blit(self.score_label,self.score_label_rect)

