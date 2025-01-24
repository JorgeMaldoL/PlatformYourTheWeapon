import pygame
import sys
from constants import *
from entities import PhysicsEntity

class Game:
    def __init__(self):    
        pygame.init()
        pygame.display.set_caption('JUMP.AI')
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

        self.clock = pygame.time.Clock()
        
        self.bacground = pygame.transform.scale(pygame.image.load("data/images/environment/background_wall.png").convert(), self.screen.get_size())
        self.left_wall = pygame.image.load('data/images/environment/left_wall.png')
        self.right_wall = pygame.image.load('data/images/environment/right_wall.png')

        self.movement = [False, False]    

        self.player = PhysicsEntity(self, 'player', (50,50), (8, 15))

    def run(self):
        while True:
            self.screen.blit(self.bacground, (50, 0))
            self.screen.blit(self.left_wall, (0, 0))
            self.screen.blit(self.right_wall, (SCREEN_WIDTH-125, 0))

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.screen)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == (pygame.K_UP or pygame.K_W):
                        self.movement[0] = True
                    if event.key == (pygame.K_DOWN or pygame.K_S):
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == (pygame.K_UP or pygame.K_W):
                        self.movement[0] = False
                    if event.key == (pygame.K_DOWN or pygame.K_S):
                        self.movement[1] = False
                
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()