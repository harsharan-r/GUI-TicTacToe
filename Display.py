import pygame
import time

width = 800
height = 800

pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
background_color_grey = '#DCDDD8'

cyan = "#00A6A6"
dark_cyan = (0, 139, 139)
background_cyan = "#006E6E"

dark_red = (139, 35, 0)
overcursor_colour = (179, 45, 0)

button_colour = dark_red


def background(game_state):	

	global button_colour

	if game_state:

		screen.fill(background_color_grey)

		pygame.draw.rect(screen,background_cyan,(260,0,10,800))
		pygame.draw.rect(screen,background_cyan,(537,0,10,800))	
		pygame.draw.rect(screen,background_cyan,(0,260,800,10))
		pygame.draw.rect(screen,background_cyan,(0,537,800,10))	
	
	else:

		screen.fill(background_color_grey)


class Button:

	def __init__(self):

		#button background 
		self.dynamic_elevation = 20
		self.button_rect = pygame.Rect(0,0,600,200)
		self.back_button_rect = pygame.Rect(0,0,600,200)
		
		#centering button background
		self.button_rect.center = (width/2,height/2)
		self.back_button_rect.center = (width/2,height/2+self.dynamic_elevation)

		#button text
		myfont = pygame.font.SysFont('Poppins-Regular', 100)
		Start_Text = 'Start Game'
		self.Start_Text_label = myfont.render(Start_Text,1,"#FEFFFA")
		self.text_rect = self.Start_Text_label.get_rect(center=(width/2, height/2))
		self.text_rect_clicked = self.Start_Text_label.get_rect(center=(width/2, height/2+self.dynamic_elevation))

		#button interaction
		self.clicked = False

	def draw(self,game_state):

		if not game_state:
			pos = pygame.mouse.get_pos()

			pygame.draw.rect(screen, background_cyan, self.back_button_rect, border_radius = 10)

			if self.button_rect.collidepoint(pos):
				
				if pygame.mouse.get_pressed()[0]:
					pygame.draw.rect(screen, cyan, self.back_button_rect, border_radius = 10)
					screen.blit(self.Start_Text_label, self.text_rect_clicked)
					self.clicked = True
				else:
					pygame.draw.rect(screen, cyan, self.button_rect, border_radius = 10)
					screen.blit(self.Start_Text_label, self.text_rect)
					if self.clicked:
						print('clicked')
						return True
			else:
				pygame.draw.rect(screen, dark_cyan, self.button_rect, border_radius = 10)
				screen.blit(self.Start_Text_label, self.text_rect)
				
		
		