import pygame.font;

class Start_Button():
	def __init__(self, screen):
		# get the screen and save it to this object
		self.screen = screen;
		# get the screens size and location
		self.screen_rect = screen.get_rect();

		# set the width of the button image
		self.width = 250;
		# set the height
		self.height = 100;
		# set the color
		self.button_color = 0,200,150;
		self.text_color = 255,255,255;
		# set the font info
		# font (font-name, font size)
		# none for font name = default 
		self.font = pygame.font.Font(None,52);

		# set the rect of the button
		# telling it to draw from (0,0) to (self.width, self.height)
		self.rect = pygame.Rect(0,0,self.width,self.height)
		# set the location of the button (center of the screen)
		self.rect.center = self.screen_rect.center;
		self.setup_message();

	def setup_message(self):
		# turn the text into an image
		# "TRUE" means message will go on top of button
		self.image_message = self.font.render("Play", True, self.text_color);
		self.image_message_rect = self.image_message.get_rect();
		self.image_message_rect.center = self.rect.center;

	def draw_button(self):
		# fill in the butotn
		self.screen.fill(self.button_color, self.rect);
		# actually draw the button
		# parameters: (what, where)
		self.screen.blit(self.image_message,self.image_message_rect);