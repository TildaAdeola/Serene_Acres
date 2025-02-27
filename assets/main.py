import sys

import pygame

pygame.init()
display = pygame.display.set_mode((480, 270))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

background = pygame.image.load("Game Objects/Background.png").convert_alpha()
floor_surf = pygame.image.load("Game Objects/Foreground.png").convert_alpha()
game_font = pygame.font.Font("Fonts/Starborn.ttf", 10) 
panel_surf = pygame.image.load("UI Elements/Panel.png").convert_alpha()
panel_rect = panel_surf.get_rect(topleft=(0, 0))
score_surf = game_font.render("Score", True, '#faf1e8')
score_rect = score_surf.get_rect(center = (130, 20))


obstacle_surf = pygame.image.load("Game Objects/Obstacle_1.png").convert_alpha()
obstacle_surf = pygame.transform.scale(obstacle_surf, (50,50))
obs_position = 500
obs_speed = -4
obs_rect = obstacle_surf.get_rect(midbottom = (obs_position, 230))


player_surf = pygame.image.load("Game Objects/Teddy_Bear.png").convert_alpha()
player_surf = pygame.transform.scale(player_surf, (70,70))
player_rect = player_surf.get_rect(midbottom = (80, 230))
player_gravity = -50


while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    # if event.type == pygame.MOUSEMOTION:
    #   print(event.pos)
    #   if player_rect.collidepoint(event.pos):
    #     print("collision")
    
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      player_gravity = -50
      
  pygame.display.update()
  display.blit(background, (0,0))
  display.blit(floor_surf, (0,10))
  display.blit(panel_surf, panel_rect)
  display.blit(score_surf,score_rect)
  
  clock.tick(60)
  
  display.blit(obstacle_surf, obs_rect)
  obs_rect.x += obs_speed
  if obs_rect.right <= 0:
    obs_rect.left = 500

  #player
  player_gravity += 1
  display.blit(player_surf, player_rect)
  player_rect.y += player_gravity
  
  
  
  
  
  