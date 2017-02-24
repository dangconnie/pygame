# A file for all our game functions to clean up main.pygame
import pygame;

# we need sys to halt the program
import sys;

def check_events(hero, start_button, game_settings):
	for event in pygame.event.get():
		# this means the user clicked on the red x
		if event.type == pygame.QUIT:
			# stop the game! the user wants off
			sys.exit();

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos();
			# print mouse_x, mouse_y;
			if start_button.rect.collidepoint(mouse_x, mouse_y):
				# check if game is active or inactive
				# if button is clicked, game_settings becomes TRUE
				game_settings.game_active = True;
				# must be a wav file to add bg music this way
				# bg_music = pygame.mixer.Sound('')
				# bg_music.play();
		# check for key press
		elif event.type == pygame.KEYDOWN:
			# print event.key;
			# user pressed a key and it's the right arrow
			if event.key == pygame.K_RIGHT:
				print "Pressed right key";
				# set the hero boolean for moving right to true
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True;
				print "Pressed left key";
			elif event.key == pygame.K_UP:
				print "Pressed up key";
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				print "Pressed down key";
				hero.moving_down = True;
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False;