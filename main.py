import pygame
# print "Pygame found!";
# we need sys to halt the program
# import sys;
# import our settings from the settings modules
from settings import Settings;

# get our hero class
from hero import Hero;

# get the check_events function from the game_functions module
from game_functions import check_events;

# from pygame, get the sprite stuff and groupcollide to handle collisions
from pygame.sprite import Group, groupcollide;

# get our enemy class
from enemy import Enemy;

# initialize all pygame modules!
pygame.init();


# 600 high, 600 wide
# screen_size = (600, 600); 
# expects a tuple that will tell the computer the size of the screen
# screen = pygame.display.set_mode(screen_size);

# make a background color.....this is the color of grass
# bg_color = (82,111,53)

# Put a message on the status bar so that the player knows the name of the game
pygame.display.set_caption("Monster attack!");

# create an object our of our Settings class
game_settings = Settings();
screen = pygame.display.set_mode(game_settings.screen_size);
# game settings now available inside main
hero = Hero(screen, game_settings);

# Make a group of enemies
enemies = Group();
enemies.add(Enemy(screen, game_settings));


# This loop will run forever
while 1:

	# run our check_events here
	check_events(hero);

	# put our bg color as the fill of our game
	screen.fill(game_settings.bg_color);

	# update the hero moving booleans
	hero.update_me();

	# draw the hero
	hero.draw_me();

	# like in canvas where we had to clear out the screen each time. (request animation frame)
	pygame.display.flip();

