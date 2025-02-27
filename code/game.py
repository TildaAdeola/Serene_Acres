import pygame, sys, os
from settings import *
from player import Player
from sprites import *
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
        pygame.display.set_caption('Serene acres')
        self.clock = pygame.time.Clock()
        self.running = True

        # Groups for drawing and collisions
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

    def setup(self):
        # Load the TMX map using an absolute path
        map = load_pygame(os.path.abspath(os.path.join('..', 'graphics', 'map stuff', 'Map.tmx')))

        # Tile layers
        for x, y, image in map.get_layer_by_name("Lake").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Ground").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Ground2").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("HighGround").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("Decor").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("DecorTop").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)
        for x, y, image in map.get_layer_by_name("HighDecor").tiles():
            Sprite((x * tile_size, y * tile_size), image, self.all_sprites)

        # Object layers
        for obj in map.get_layer_by_name("natural collisions"):
            CollisionSprite((obj.x, obj.y), obj.image, self.all_sprites, self.collision_sprites)
        for obj in map.get_layer_by_name("interaction objects"):
            CollisionSprite((obj.x, obj.y), obj.image, self.all_sprites, self.collision_sprites)
        for obj in map.get_layer_by_name("Hitboxes"):
            # Add to both groups so these are drawn
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.all_sprites, self.collision_sprites)
        for obj in map.get_layer_by_name("Entities"):
            if obj.name == "Player":
                self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000  # seconds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

def Main_game():
    if __name__ == "__main__":
        game = Game()
        game.run()

Main_game()
