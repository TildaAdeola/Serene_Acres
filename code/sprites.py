import pygame
from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, *group):
        super().__init__(*group)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.Ground = True

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, *groups, scale_factor=2):
        super().__init__(*groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)
        self.display_surface = pygame.display.get_surface()
        self.scale_factor = scale_factor


