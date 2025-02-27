import pygame
from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self, scale_factor=2):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2(0, 0)
        self.scale_factor = scale_factor

    def draw(self, target_pos):
        # Apply offset before scaling to keep movement accurate
        self.offset.x = (-target_pos[0]) + (self.display_surface.get_width() // (2 * self.scale_factor))
        self.offset.y = (-target_pos[1]) + (self.display_surface.get_height() // (2 * self.scale_factor))

        #camera stuff, Basic camera and y-sort
        ground_sprites = [sprite for sprite in self if hasattr(sprite, 'ground')]
        object_sprites = [sprite for sprite in self if not hasattr(sprite, 'ground')]

        for layer in [ground_sprites, object_sprites]:

            for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
                # Scale the sprite image
                scaled_image = pygame.transform.scale(
                    sprite.image, (int(sprite.rect.width * self.scale_factor), int(sprite.rect.height * self.scale_factor))
                )

                # Scale the position
                scaled_pos = (sprite.rect.topleft + self.offset) * self.scale_factor

                self.display_surface.blit(scaled_image, scaled_pos)

