import pygame


class ShipExplosion:
    """
    Creating an explosion for the player ship using a sprite sheet.
    """

    def __init__(self, settings):
        self.settings = settings  # get the settings stuff
        self.frames = (
            self._load_frames()
        )  # call the helper function to slice up the sprite sheet
        self.frame_index = 0  # tracks the sprite
        self.last_update = 0  # tracks time for the sprite being used
        self.active = False  # lets the main app know if the explosion if happening
        self.rect = self.frames[0].get_rect()  # sizes the explosion

    def _load_frames(self):

        # loads the whole sprite sheet into memory and optimizes it
        sheet = pygame.image.load(self.settings.explosion_file).convert()
        sheet_w, sheet_h = sheet.get_size()  # gets size of the sprite sheet
        frame_w = sheet_w // 4  # divides the sprite sheet up
        frame_h = sheet_h // 4  # same as above, to get size of individual sprite

        frames = list()  # list for the sprite images
        for row in range(4):
            for col in range(4):  # loops through all the sprites
                # defines the box for the sprite sheet
                rect = pygame.Rect(col * frame_w, row * frame_h, frame_w, frame_h)
                frame = sheet.subsurface(rect).copy()  # cuts out the individual sprite
                frame.set_colorkey((0, 0, 0))  # set black as transparent
                frame = pygame.transform.scale(
                    frame,  # resizes the cut out to match the size of the explosion
                    (self.settings.explosion_size, self.settings.explosion_size),
                )
                frames.append(frame)  # adds finished frame to the frames list
        return frames  # send the list of the images to self.frames in the __init__

    def start(self, center_pos):
        """
        Trigger the explosion where the ship was located.
        """
        self.rect.center = (
            center_pos  # makes sure the explosion is centered on the ship
        )
        self.frame_index = 0  # resets back to the initial frame for 2nd and 3rd lives
        self.last_update = (
            pygame.time.get_ticks()
        )  # makes sure the whole explosion is visible
        self.active = True  # lets the explosion happen

    def update(self):
        """
        Display all the images in the explosion and turns it off when it finishes.
        """
        if not self.active:  # exit if not currently exploding
            return
        now = pygame.time.get_ticks()  # get the current time
        if (
            now - self.last_update >= self.settings.explosion_frame_delay
        ):  # timing check
            self.last_update = now  # reset for next frame
            self.frame_index += 1  # advance to the next image
            if self.frame_index >= len(self.frames):
                self.active = (
                    False  # when it hits the last image, turn off the animation
                )

    def draw(self, screen):
        """
        Draw the explosion frame if active.
        """
        if self.active:  # check for active status
            screen.blit(
                self.frames[self.frame_index], self.rect
            )  # draw the image in the right place
