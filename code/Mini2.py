import pygame
import random
import os
from game import Game

class RecipeMemoryGame(Game):
    def __init__(self):
        super().__init__()
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 800, 600
        # Create a window (display surface) with the given dimensions
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # Set the title of the game window
        pygame.display.set_caption("Recipe Memory Game")
        # Create a clock object to help manage the game's frame rate
        self.clock = pygame.time.Clock()

        # ------------------------------
        # Define Colors (for text and other UI elements)
        # ------------------------------
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)

        # ------------------------------
        # Set up Font for text rendering
        # ------------------------------
        # None means use the default pygame font; 36 is the font size
        self.FONT = pygame.font.Font(None, 36)

        # ------------------------------
        # Define Ingredients and Load their Images
        # ------------------------------
        # List of ingredient names
        self.ingredients = ["Tomato", "Flour", "Cheese", "Egg", "Milk"]

        # Load images for each ingredient.
        # NOTE: Replace the file paths with the correct paths for your assets.
        self.ingredient_images = {
            "Tomato": pygame.image.load(os.path.join("assets", "tomato.png")).convert_alpha(),
            "Flour": pygame.image.load(os.path.join("assets", "flour.png")).convert_alpha(),
            "Cheese": pygame.image.load(os.path.join("assets", "cheese.png")).convert_alpha(),
            "Egg": pygame.image.load(os.path.join("assets", "egg.png")).convert_alpha(),
            "Milk": pygame.image.load(os.path.join("assets", "milk.png")).convert_alpha()
        }

        # ------------------------------
        # Scale Images and Create Rectangles for Collision Detection
        # ------------------------------
        # We'll display each ingredient image at a fixed size (e.g., 100x100 pixels)
        self.ingredient_rects = {}  # Dictionary to store the rect (position and size) for each ingredient image
        for i, ingredient in enumerate(self.ingredients):
            # Scale the image to 100x100 pixels
            scaled_image = pygame.transform.scale(self.ingredient_images[ingredient], (100, 100))
            # Update the dictionary with the scaled image
            self.ingredient_images[ingredient] = scaled_image
            # Create a rectangle for the image for positioning and collision detection.
            # Here we position the images horizontally with a starting x-coordinate of 100 and y-coordinate of 400.
            # The x-coordinate for each subsequent ingredient is increased by 120 pixels.
            rect = scaled_image.get_rect(topleft=(100 + i * 120, 400))
            # Save the rectangle in the dictionary with the ingredient name as the key.
            self.ingredient_rects[ingredient] = rect

        # ------------------------------
        # Initialize Game Variables
        # ------------------------------
        self.level = 1  # The starting level (affects recipe length)
        self.recipe = []  # List that will hold the current recipe (sequence of ingredients)
        self.player_selection = []  # List to record the ingredients the player selects
        self.running = True  # Flag to control the main game loop
        self.show_recipe = True  # Flag to control whether the recipe is being displayed to the player
        self.feedback_message = ""  # Feedback message to display (e.g., "Correct!" or "Try Again!")

        # Generate the first recipe to start the game
        self.reset_game()

    def generate_random_recipe(self, length):
        """
        Generate a random recipe sequence by randomly selecting ingredients.

        Parameters:
            length (int): The number of ingredients in the recipe.

        Returns:
            list: A list of ingredient names representing the recipe.
        """
        # Use random.sample to get a list of unique ingredients of the specified length
        return random.sample(self.ingredients, length)

    def display_recipe(self, recipe):
        """
        Display the current recipe as text at the top of the screen.

        Parameters:
            recipe (list): The recipe list to display.
        """
        # Join the list elements into a string separated by arrows
        recipe_text = " -> ".join(recipe)
        # Render the text surface with the recipe string
        text_surface = self.FONT.render(f"Recipe: {recipe_text}", True, self.BLACK)
        # Blit (draw) the text onto the screen at position (20, 50)
        self.screen.blit(text_surface, (20, 50))

    def display_feedback(self, message, color):
        """
        Display a feedback message (e.g., "Correct!" or "Try Again!") in the center of the screen.

        Parameters:
            message (str): The feedback message to display.
            color (tuple): The color to use for the text.
        """
        # Render the feedback text surface
        feedback_surface = self.FONT.render(message, True, color)
        # Get a rect for the text surface and center it on the screen
        feedback_rect = feedback_surface.get_rect(center=(self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT // 2))
        # Blit the text onto the screen at the calculated position
        self.screen.blit(feedback_surface, feedback_rect)

    def reset_game(self):
        """
        Reset the game state for the next round.
        This includes generating a new recipe and clearing player selections.
        """
        # Increase the recipe length with the level (level + 2 gives a growing challenge)
        self.recipe = self.generate_random_recipe(self.level + 2)
        # Clear the player's previous selections
        self.player_selection = []
        # Clear any previous feedback message
        self.feedback_message = ""
        # Set the flag to show the recipe at the beginning of the round
        self.show_recipe = True

    def run(self):
        """
        The main game loop for the Recipe Memory Game.
        Handles events, updates game state, and renders everything to the screen.
        """
        while self.running:
            # Clear the screen by filling it with white
            self.screen.fill(self.WHITE)

            # ------------------------------
            # Event Handling Section
            # ------------------------------
            for event in pygame.event.get():
                # Check if the user has requested to close the window
                if event.type == pygame.QUIT:
                    self.running = False  # Set the running flag to False to exit the game loop

                # Process mouse clicks only when the recipe is not being shown
                if event.type == pygame.MOUSEBUTTONDOWN and not self.show_recipe:
                    # Loop through each ingredient and its associated rectangle
                    for ingredient, rect in self.ingredient_rects.items():
                        # Check if the mouse click occurred within the area of the ingredient image
                        if rect.collidepoint(event.pos):
                            # Append the ingredient to the player's current selection
                            self.player_selection.append(ingredient)
                            # ------------------------------
                            # Check if the player's selection matches the recipe
                            # ------------------------------
                            if self.player_selection == self.recipe:
                                # If the selection is correct, update the feedback message
                                self.feedback_message = "Correct!"
                                # Increase the level to make the recipe longer next round
                                self.level += 1
                                # Pause briefly so the player can see the "Correct!" message
                                pygame.time.wait(1000)
                                # Reset the game for the next round
                                self.reset_game()
                            # If the number of selections equals the recipe length but does not match
                            elif len(self.player_selection) == len(self.recipe):
                                # Provide negative feedback
                                self.feedback_message = "Try Again!"
                                # Pause briefly so the player can read the feedback
                                pygame.time.wait(1000)
                                # Reset the game so the player can try the same recipe again
                                self.reset_game()

            # ------------------------------
            # Drawing Section: Render Ingredient Images and Text
            # ------------------------------
            # Loop through all ingredients to display their images
            for ingredient in self.ingredients:
                # Retrieve the scaled image for the ingredient
                image = self.ingredient_images[ingredient]
                # Retrieve the rect for positioning and collision detection
                rect = self.ingredient_rects[ingredient]
                # Draw (blit) the ingredient image onto the screen at its designated position
                self.screen.blit(image, rect)
                # Optionally, draw the ingredient's name below the image for clarity
                label_surface = self.FONT.render(ingredient, True, self.BLACK)
                # Center the label horizontally beneath the image and adjust vertically
                label_rect = label_surface.get_rect(center=(rect.centerx, rect.bottom + 20))
                self.screen.blit(label_surface, label_rect)

            # ------------------------------
            # Display Recipe or Feedback
            # ------------------------------
            if self.show_recipe:
                # If the recipe should be shown (e.g., at the beginning of a round), display it
                self.display_recipe(self.recipe)
                # Update the display immediately so the recipe appears
                pygame.display.flip()
                # Wait for 3000 milliseconds (3 seconds) so the player can memorize the recipe
                pygame.time.wait(3000)
                # After showing, hide the recipe so the player can start selecting ingredients
                self.show_recipe = False
            elif self.feedback_message:
                # If there's a feedback message, display it in the center of the screen
                # Use GREEN color for a "Correct!" message and RED for a "Try Again!" message
                if self.feedback_message == "Correct!":
                    self.display_feedback(self.feedback_message, self.GREEN)
                else:
                    self.display_feedback(self.feedback_message, self.RED)

            # ------------------------------
            # Update the Display and Maintain Frame Rate
            # ------------------------------
            # Flip the display buffers to update the screen with all drawn elements
            pygame.display.flip()
            # Cap the frame rate at 30 frames per second
            self.clock.tick(30)

        # When the game loop ends (e.g., user closed the window), quit pygame
        pygame.quit()


if __name__ == "__main__":
    # Create an instance of RecipeMemoryGame and start the game loop
    game = RecipeMemoryGame()
    game.run()

