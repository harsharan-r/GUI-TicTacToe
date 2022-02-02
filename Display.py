import pygame
import time
import os

#setting width and height of the window
width = 800
height = 800

#instializing pygame and creating windows and setting clock
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#colour referneces
white = (255,255,255)
black = (0,0,0)
background_color_grey = '#DCDDD8'

cyan = "#00A6A6"
dark_cyan = (0, 139, 139)
background_cyan = "#006E6E"

dark_red = (139, 35, 0, 240)
overcursor_colour = (179, 45, 0)


#function to control background
def background(game_state):	

	line_thickiness = 10

	if game_state:

		screen.fill(background_color_grey)

		pygame.draw.rect(screen,background_cyan,(260,0,line_thickiness,800))
		pygame.draw.rect(screen,background_cyan,(530,0,line_thickiness,800))	
		pygame.draw.rect(screen,background_cyan,(0,260,width,line_thickiness))
		pygame.draw.rect(screen,background_cyan,(0,530,width,line_thickiness))	
	
	else:

		screen.fill(background_color_grey)

#class which displays and monitors when the button on the main menu is clicked
class Button:

	def __init__(self,dimensions,pos,text,font_size,dynamic_elevation,colour=cyan,background_colour=background_cyan,border_radius=10,IF_OFF=10):

		self.button_click_sound = pygame.mixer.Sound(os.path.join("Assets","Button_Press.mp3"))
		self.button_release_sound = pygame.mixer.Sound(os.path.join("Assets","Button_Release.mp3"))

		self.button_click_sound.set_volume(0.7)
		self.button_release_sound.set_volume(0.7)

		#button background 
		self.dynamic_elevation = dynamic_elevation
		self.button_rect = pygame.Rect(0,0,dimensions[0],dimensions[1])
		self.back_button_rect = pygame.Rect(0,0,dimensions[0],dimensions[1])
		
		#centering button background
		self.button_rect.center = (pos[0],pos[1])
		self.back_button_rect.center = (pos[0],pos[1]+self.dynamic_elevation)

		#animated buttons
		self.button_rect_hover = self.button_rect.inflate(IF_OFF,IF_OFF)
		self.back_button_rect_hover = self.back_button_rect.inflate(IF_OFF,IF_OFF)

		#button text
		myfont = pygame.font.SysFont('Poppins-Regular', font_size)
		self.Start_Text_label = myfont.render(text,1,"#FEFFFA")
		self.text_rect = self.Start_Text_label.get_rect(center=(pos[0],pos[1]))
		self.text_rect_clicked = self.Start_Text_label.get_rect(center=(pos[0], pos[1]+self.dynamic_elevation))

		#button interaction
		self.clicked = False

	def draw(self):

		#if not game_state:
		pos = pygame.mouse.get_pos()


		#drawing the shaded part of the button
		

		#checks if you mouse is over the button
		if self.button_rect.collidepoint(pos):
			
			#checks if you are clicking the button
			if pygame.mouse.get_pressed()[0]:
				pygame.draw.rect(screen, cyan, self.back_button_rect_hover, border_radius = 10)
				screen.blit(self.Start_Text_label, self.text_rect_clicked)
				
				if not self.clicked:
					self.button_click_sound.play()
				self.clicked = True

			else:		
				pygame.draw.rect(screen, background_cyan, self.back_button_rect_hover, border_radius = 10)
				pygame.draw.rect(screen, cyan, self.button_rect_hover, border_radius = 10)
				screen.blit(self.Start_Text_label, self.text_rect)
				#returns the button is clicked when you have let go of the button
				if self.clicked:
					self.button_click_sound.stop()
					self.button_release_sound.play()
					return True
		else:
			pygame.draw.rect(screen, background_cyan, self.back_button_rect, border_radius = 10)
			pygame.draw.rect(screen, dark_cyan, self.button_rect, border_radius = 10)
			screen.blit(self.Start_Text_label, self.text_rect)
			self.button_click_sound.stop()
			self.button_release_sound.stop()

class Menu:

	def __init__(self, dimensions, pos, colour, text, text_pos, text_size=0, auto_text_size=False):

		self.menu = pygame.Rect((0,0),dimensions)
		self.menu.center = pos
		self.text_string = text
		self.text_size = text_size
		self.text_pos = text_pos
		self.font = pygame.font.SysFont('Poppins-Regular', text_size)
		self.colour = colour

		while(auto_text_size):
			if self.font.size(text)[0] < dimensions[0] - 10 and self.font.size(text)[1] < dimensions[1] - 10:
				self.text_size+=1
			elif self.font.size(text)[0] > dimensions[0] - 5 and self.font.size(text)[1] > dimensions[1] - 5:
				self.text_size+=1
			else:
				break

			self.font = pygame.font.SysFont('Poppins-Regular', self.text_size)

		self.text_label = self.font.render(text,1,"#FEFFFA")
		self.text_rect = self.text_label.get_rect(center=text_pos)

	def draw_rect_alpha(self, surface, color, rect, corner_radius):
	    shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
	    pygame.draw.rect(shape_surf, color, shape_surf.get_rect(), border_radius=corner_radius)
	    surface.blit(shape_surf, rect)

	def draw(self):

		self.draw_rect_alpha(screen, self.colour, self.menu, 10)
		screen.blit(self.text_label, self.text_rect)
