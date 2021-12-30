import pygame
from Display import *
import os

class Game:

	def __init__(self):
		self.board = [[i,0] for i in range(9)]
		self.selected_square = 0

		sqr_pos = [0,270,540]
		sqr_height, sqr_width = 260, 260
		self.square_pos = [pygame.Rect(i,j,sqr_width,sqr_height) for i in sqr_pos for j in sqr_pos]

		X_image = pygame.image.load(os.path.join('Assets','X.png'))
		O_image = pygame.image.load(os.path.join('Assets','O.png'))

		self.X_Obj = pygame.transform.scale(X_image,(sqr_height,sqr_width))
		self.O_Obj = pygame.transform.scale(O_image,(sqr_height,sqr_width))

		#player one will be X and player 2 will be O
		self.player = 1
		self.current_piece = 'X'

		self.clicked = False

	def draw(self):
		for i,j in self.board:
			if j == 'X':
				X_rect = self.X_Obj.get_rect(center = self.square_pos[i].center)
				screen.blit(self.X_Obj, X_rect)
				#blit X onto respective square 

			elif j == 'O':
				O_rect = self.O_Obj.get_rect(center = self.square_pos[i].center)
				screen.blit(self.O_Obj, O_rect)
				#blit O onto respective square

	def mouse_hover(self):
		pos = pygame.mouse.get_pos()
		for i in range(len(self.square_pos)):
			if self.square_pos[i].collidepoint(pos) and self.board[i][1] == 0:

				self.selected_square = i

				if self.current_piece == "X":
					X_rect = self.X_Obj.get_rect(center = self.square_pos[i].center)
					screen.blit(self.X_Obj, X_rect)
				else:
					O_rect = self.O_Obj.get_rect(center = self.square_pos[i].center)
					screen.blit(self.O_Obj, O_rect)
				

	def update(self):
		
		if pygame.mouse.get_pressed()[0]:
			self.clicked = True

		else:
			if self.clicked:
				self.board[self.selected_square][1] = self.current_piece
				self.player = 1 if self.player == 0 else 0
				self.clicked = False

		self.current_piece = 'X' if self.player == 1 else 'O'

		self.mouse_hover()
		self.draw()