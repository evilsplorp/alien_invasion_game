import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """A class to manage individual bullets fired from the player's ship."""

    def __init__(self, fleet: "AlienFleet", x: float, y: float):
        """Initialize the bullet sprite, load it, and make sure it launches from the ship's midtop."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # original image control
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_w, self.settings.alien_h)
        )

        # new alien images control
        image_1 = pygame.image.load(self.settings.alien_file)
        image_1 = pygame.transform.scale(
            image_1, (self.settings.alien_w, self.settings.alien_h)
        )

        image_2 = pygame.image.load(self.settings.alien_file_2)
        image_2 = pygame.transform.scale(
            image_2, (self.settings.alien_w, self.settings.alien_h)
        )

        self.images = list((image_1, image_2))
        self.image_index = 0
        self.image = self.images[self.image_index]

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def swap_image(self):
        """Toggles between the two images"""
        self.image_index = (self.image_index + 1) % len(self.images)
        self.image = self.images[self.image_index]

    def update(self):
        """Move the bullet up and update its exact position."""

        temp_speed = self.settings.fleet_speed

        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """
        Locate the edges of the screen.
        """
        return (
            self.rect.right >= self.boundaries.right
            or self.rect.left <= self.boundaries.left
        )

    def draw_alien(self):
        """Generate the alien image onto the screen surface at its updated position."""

        self.screen.blit(self.image, self.rect)
