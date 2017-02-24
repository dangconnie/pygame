import pygame;
from pygame.sprite import Sprite;
import math;

class Enemy(Sprite):
	def __init__(self,screen, game_settings):
		super(Enemy, self).__init__();
		# load the image
		self.image = pygame.image.load('monster1.png');
		# set the speed
		self.speed = 2;
		# find the location and size of the image just loaded
		self.rect = self.image.get_rect();
		# find the location and size of the screen
		self.screen_rect = screen.get_rect();
		# set up the screen
		self.screen = screen;
		# set the center of the image..
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;

	def update_me(self,hero):
		# we want the enemy moving relative to the hero (chasing it) since this is a shooting game. dx = delta x or change in x
		dx = self.rect.x - hero.rect.x;
		# think of x-axis and y-axis
		dy = self.rect.y - hero.rect.y;
		# figure out the diff between the hero's x and the enemy's x and the hero's y and enemy's y to find the hypotenuse
		dist = math.hypot(dx,dy);
		# need the enemy to move on the hypotenuse to go towards hero so...
		dx = dx / dist;
		dy = dy / dist;

		self.rect.x -= dx * self.speed;
		self.rect.y -= dy * self.speed;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);
