import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.image.set_colorkey(self.image.get_at((0, 0)))  # Transparent color key

        # Movement flag
        self.moving_right = False

    def update(self):
        """Update the ship's position if moving right."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 5  # Move the ship to the right by 5 pixels

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
