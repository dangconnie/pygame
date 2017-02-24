import pygame;
from pygame.sprite import Sprite;

class Enemy(Sprite):
	def __init__(self,screen, game_settings):
		super(Enemy, self).__init__();