# First file in our project
# Will create a simple window

import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))

    # Set the background color.
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Make a ship.
    ship = Ship(ai_settings, screen)

    pygame.display.set_caption("Alien Invasion")
    # Start the main loop for the game.
    # Everything happens here
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
