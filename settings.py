from pathlib import Path

class Settings:
    """A class to manage all the global settings for the game."""

    def __init__(self):
        self.name: str = 'Alien Invasion Purple Edition'
        self.screen_w = 1200
        # original size
        # self.screen_h = 800 
        self.screen_h = 1200
        self.FPS = 60
        # original background
        # self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'purple_background_2.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        # original ship
        # self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'new_ship.png'
        # original ship size
        # self.ship_w = 40
        self.ship_w = 60
        self.ship_h = 60

        # original bullet
        # self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'new_laser_2.png'
        # original bullet sound
        # self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'new_laser2.mp3'     
        # original explosion sound   
        # self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'explosion3.mp3'
        
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1
        
        self.button_w = 200
        self.button_h = 65
        self.button_color = (255, 255, 255)
        # self.button_color = (97, 14, 182)

        # added button_text_color to differentiate from text_color for HUD
        self.button_text_color = (97, 14, 182)
        self.text_color = (255, 255, 255)
        self.button_font_size = 36
        self.HUD_font_size = 14
        # self.font_file = Path.cwd() / 'Assets' / 'fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'
        self.font_file = Path.cwd() / 'Assets' / 'fonts' / 'Righteous' / 'Righteous.ttf'

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 5
        self.starting_ship_count = 3

        self.bullet_w = 25
        self.bullet_h = 80   
        self.bullet_speed = 7
        self.bullet_amount = 5

        self.fleet_speed = 2
        self.fleet_drop_speed = 40
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale

