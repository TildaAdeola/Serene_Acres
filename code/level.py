import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):

        #getting the display surface
        self.display_surface = pygame.display.get_surface()

        #sprite group
        self.all_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        self.player = Player((40,200), self.all_sprites)


    def run(self, dt):
        self.display_surface.fill('black') #so we don't accidentally see the previous frame
        self.all_sprites.draw(self.display_surface) #creating a place to draw sprites on and in this case, the display surface we created earlier
        self.all_sprites.update() #updates the sprites just like we update the screen



