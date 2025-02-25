# alien_invasion.py
import pygame
import sys
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in.
    bullets = Group()

    #Make an Alien
    alien = Alien(ai_settings, screen)

    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    print("Game is running...")
    
    while True:
        gf.check_events(ship, ai_settings, screen, bullets)  # Handle user inputs
        ship.update()  # Update ship position
        bullets.update()  # Update bullets
        gf.update_bullets(aliens, bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)  # Redraw the screen

try:
    run_game()
except Exception as e:
    print(f"An error occurred: {e}")
    pygame.quit()
    sys.exit()
