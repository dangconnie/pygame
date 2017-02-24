import pygame;

# This will get the Sprite class from pygame.sprite. Our hero will be a sprite object
from pygame.sprite import Sprite;

class Hero(Sprite):
	# initalize class properties. WE need hero to know about the screen here and on main.py
	def __init__(self, screen, settings):
		super(Hero,self).__init__();
		self.image = pygame.image.load("hero.png");
		# resize dude 
		# self.image = pygame.transform.scale(self.image,(100, 100))
		# now that we have the screen, let's give the screen to our hero
		self.screen = screen;
		# create a rect prop that will be the dimensions and location of hero
		# it's available in get_rect because this is a pygame image
		self.rect = self.image.get_rect();
		# Now that we have the screen object from main, get the size of the screen
		self.screen_rect = screen.get_rect();
		print self.screen_rect;
		# this will put the middle of the hero at the middle of the screen
		# we're putting hero relative to screen size
		self.rect.centery = self.screen_rect.centery;
		# this will put the left side of our hero at the left side of our screen
		self.rect.left = self.screen_rect.left;
		# set up the movement booleans. All are false at init
		self.moving_right = False;
		self.moving_left = False;
		self.moving_up = False;
		self.moving_down = False;
		self.speed = settings.hero_speed_modifier;

	def update_me(self):
		# if user is pushing left, move my self.rect left and so on...
		if self.moving_right:
			# the hero moving_right boolean is true so update the hero's location
			self.rect.centerx += 10 * self.speed;
		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed;

		if self.moving_down:
		# the hero moving_down boolean is true so update the hero's location
			self.rect.centery += 10 * self.speed;
		elif self.moving_up:
			self.rect.centery -= 10 * self.speed;

	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect);
