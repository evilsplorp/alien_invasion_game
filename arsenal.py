import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """A class to manage ammunition systems, active bullets , and firing restrictions."""
    
    def __init__(self, game: 'AlienInvasion'):
        """Initialize the arsenal subsystem and set up a sprite group to manage bullets."""

        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update the position of all active bullets and remove bullets that have left the screen."""

        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """Iterate through a copy of the projectile group to delete bullets that leave the viewport."""

        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Display the active bullets from the sprite group on the game screen."""

        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Generate and register a new bullet if the current active count is under the bullet limit."""

        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False