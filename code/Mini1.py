import sys
import pygame
import os
from game import Game


class EndlessRunner(Game):
    def __init__(self):
        # Initialize the main game first
        super().__init__()
        # Override the window size and caption for the mini-game
        self.screen = pygame.display.set_mode((480, 270))
        pygame.display.set_caption("Mini Game")
        self.clock = pygame.time.Clock()

        # Load mini-game assets
        self.background = pygame.image.load(
            os.path.join("..", "assets", "Game Objects", "Background.png")).convert_alpha()
        self.floor_surf = pygame.image.load(
            os.path.join("..", "assets", "Game Objects", "Foreground.png")).convert_alpha()
        self.game_font = pygame.font.Font(os.path.join("..", "assets", "Fonts", "Starborn.ttf"), 10)
        self.panel_surf = pygame.image.load(os.path.join("..", "assets", "UI Elements", "Panel.png")).convert_alpha()
        self.panel_rect = self.panel_surf.get_rect(topleft=(0, 0))

        self.obstacle_surf = pygame.image.load(
            os.path.join("..", "assets", "Game Objects", "Obstacle_1.png")).convert_alpha()
        self.obstacle_surf = pygame.transform.scale(self.obstacle_surf, (50, 50))

        self.player_surf = pygame.image.load(
            os.path.join("..", "assets", "Game Objects", "Teddy_Bear.png")).convert_alpha()
        self.player_surf = pygame.transform.scale(self.player_surf, (70, 70))

        self.reset_mini_game()

    def reset_mini_game(self):
        """Reset mini-game variables for a new session."""
        self.obs_speed = -4
        self.obs_rect = self.obstacle_surf.get_rect(midbottom=(500, 230))
        self.player_rect = self.player_surf.get_rect(midbottom=(80, 230))
        self.player_gravity = 0
        self.score = 0
        self.mini_game_active = True

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # While the mini-game is active, allow jumping with SPACE
                if self.mini_game_active:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        if self.player_rect.bottom >= 230:
                            self.player_gravity = -50
                # If game over, pressing SPACE resets the mini-game
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.reset_mini_game()

            if self.mini_game_active:
                # Update player physics (simulate gravity)
                self.player_gravity += 1
                self.player_rect.y += self.player_gravity
                if self.player_rect.bottom >= 230:
                    self.player_rect.bottom = 230
                    self.player_gravity = 0

                # Move obstacle
                self.obs_rect.x += self.obs_speed
                if self.obs_rect.right <= 0:
                    self.obs_rect.left = 500

                # Check for collisions
                if self.player_rect.colliderect(self.obs_rect):
                    self.mini_game_active = False

                # Update score gradually
                self.score += 0.01

                # Draw mini-game elements
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(self.floor_surf, (0, 10))
                self.screen.blit(self.panel_surf, self.panel_rect)
                score_display = self.game_font.render(f"Score: {int(self.score)}", True, "#faf1e8")
                score_rect = score_display.get_rect(center=(130, 20))
                self.screen.blit(score_display, score_rect)
                self.screen.blit(self.obstacle_surf, self.obs_rect)
                self.screen.blit(self.player_surf, self.player_rect)
            else:
                # Game Over screen
                self.screen.fill((94, 129, 162))
                game_over_surf = self.game_font.render("Game Over", True, "#faf1e8")
                game_over_rect = game_over_surf.get_rect(center=(240, 135))
                self.screen.blit(game_over_surf, game_over_rect)

            pygame.display.update()
            self.clock.tick(60)


Mini1 = EndlessRunner()
Mini1.run()