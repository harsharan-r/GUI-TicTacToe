import pygame
from Display import *
import os

class Game:

	def __init__(self):
		#list of which board squares are occupied
		self.board = [[i,0] for i in range(9)]

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

	def draw(self):
		for i,j in self.board:
			if j == 'X':
				#print X onto respective squares 
				X_rect = self.X_Obj.get_rect(center = self.square_pos[i].center)
				screen.blit(self.X_Obj, X_rect)

			elif j == 'O':
				#print O onto respective square
				O_rect = self.O_Obj.get_rect(center = self.square_pos[i].center)
				screen.blit(self.O_Obj, O_rect)
				

	def mouse_hover(self):
		pos = pygame.mouse.get_pos()
		#goes through each square to check if the cursor is over it
		for i in range(len(self.square_pos)):

			#if the cursor is over a square
			if self.square_pos[i].collidepoint(pos) and self.board[i][1] == 0:

				#records the square your cursor is on
				self.selected_square = i

				#shows a preview of the piece in the square you are hovering over
				if self.current_piece == "X":
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
		
		#checks if you click a square
		if pygame.mouse.get_pressed()[0]:
			self.clicked = True

		else:
			#when you let go of the mouse button it will record the square you are over and place your piece on it
			if self.clicked:
				self.board[self.selected_square][1] = self.current_piece
				self.player = 1 if self.player == 0 else 0
				self.clicked = False

		#changing current piece depending on whos turn it is
		self.current_piece = 'X' if self.player == 1 else 'O'

		#updating graphics
		self.mouse_hover()
		self.draw()