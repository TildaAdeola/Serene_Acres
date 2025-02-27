import pygame, os
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_sprites):
        super().__init__(group)

        image_path = os.path.join("..","graphics", "char1.png")
        self.image = pygame.image.load(image_path).convert_alpha() #creating the player surface
        self.rect = self.image.get_frect(center = pos) # a rectangle for positioning


        #movement
        self.direction = pygame.Vector2(1,0)
        self.speed = 250
        self.collision_sprites =  collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    def move(self,dt):
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')



    def collision(self, direction):
        for sprite in self.collision_sprites: #getting all obstacles
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0 : self.rect.right = sprite.rect.left
                    if self.direction.x < 0 : self.rect.left = sprite.rect.right
                if direction == 'vertical':
                    if self.direction.y > 0 : self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom


    def update(self, dt):
        self.input()
        self.move(dt)







