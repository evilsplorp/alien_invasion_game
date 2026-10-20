import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to manage individual bullets fired from the player's ship."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initialize the bullet sprite, load it, and make sure it launches from the ship's midtop."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y  = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up and update its exact position."""
        
        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        return (self.rect.right >= self.boundaries.right or self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """Generate the alien image onto the screen surface at its updated position."""

        self.screen.blit(self.image, self.rect)
