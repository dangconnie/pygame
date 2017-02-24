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

# get the start button
from Button import Start_Button;

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

# Make a group for the hero to belong to so that we can use groupcollide
hero_group = Group();
hero = Hero(screen, game_settings);
# put hero into the group
hero_group.add(hero);

# Make a group of enemies
enemies = Group();
enemies.add(Enemy(screen, game_settings));

# Make a start button
start_button = Start_Button(screen);
# start_button.draw_button();

# This loop will run forever
while 1:

	# run our check_events here
	check_events(hero, start_button, game_settings);

	# put our bg color as the fill of our game
	screen.fill(game_settings.bg_color);

	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me();
		hero.draw_me();

	# update the hero moving booleans
	# hero.update_me();

	# draw the hero
	# hero.draw_me();

	# draw the enemy! our enemy is inside a list. we can't just do enemy.draw_me(). loop through the list of sprites in the enemies group
	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero);
		enemy.draw_me();

	# hero_died will be a dictionary. that dictionary is the overlap of the items in group 1(hero_died) and group2(enemies). hero_group and enemies are groups. True and True are dokill1 and dokill2. (look at documentation of groupcollide)
	hero_died = groupcollide(hero_group, enemies, True, True);
	if hero_died:
		print "You lost!";
		game_settings.game_active = False;

	if game_settings.game_active == False:	
		start_button.draw_button();

	# like in canvas where we had to clear out the screen each time. (request animation frame)
	pygame.display.flip();

