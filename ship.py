#ship.py
import pygame
import os
import sys

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and check if it exists
        ship_image_path = 'images/ship.bmp'
        if not os.path.exists(ship_image_path):
            print(f"Error: Ship image not found at {ship_image_path}")
            pygame.quit()
            sys.exit()

        self.image = pygame.image.load(ship_image_path).convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Make background color of image transparent
        self.image.set_colorkey(self.image.get_at((0, 0)))

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)




