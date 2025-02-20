import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ship)  # Pass the ship object here
        ship.update()  # Update ship position
        # Redraw the screen.
        gf.update_screen(ai_settings, screen, ship)

run_game()
