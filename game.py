import pygame
import sys
from utils import load_image
from constants import *
from entities import PhysicsEntity

class Game:
    def __init__(self):    
        pygame.init()  # Initialize all pygame modules
        pygame.display.set_caption('JUMP.AI')  # Set the window title
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Set up the display surface

        self.clock = pygame.time.Clock()  # Create a clock to manage the frame rate
        
        # Load and scale background image
        self.bacground = pygame.transform.scale(
            pygame.image.load("data/images/environment/background_wall.png").convert(), 
            self.screen.get_size()
        )
        self.left_wall = pygame.image.load('data/images/environment/left_wall.png')  # Load left wall image
        self.right_wall = pygame.image.load('data/images/environment/right_wall.png')  # Load right wall image

        self.movement = [False, False]  # Track left and right movement

        # Load player asset
        self.assets = {
            'player': load_image('characters/bot.png')
        }

        # Initialize player entity with position and size
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        while True:
            self.screen.blit(self.bacground, (50, 0))  # Draw background
            self.screen.blit(self.left_wall, (0, 0))  # Draw left wall
            self.screen.blit(self.right_wall, (SCREEN_WIDTH - 125, 0))  # Draw right wall

            # Update player position based on movement flags
            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)  # Render player on screen
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Quit pygame
                    sys.exit()  # Exit the program
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True  # Start moving left
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True  # Start moving right
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False  # Stop moving left
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False  # Stop moving right
                

            pygame.display.update()
            self.clock.tick(60)

Game().run()