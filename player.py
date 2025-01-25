import pygame
from constants import *

class Player:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load('data/images/characters/bot.png').convert_alpha(), (100,140))
        self.width = 80
        self.height = 120
        self.rect = pygame.Rect(0,0,self.width, self.height)
        self.rect.center = (x, y)
        self.flip = False

    def move(self):
        #reset variable
        dx = 0
        dy = 0

        #process the keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 10
            self.flip = True
        if key[pygame.K_d]:
            dx += 10
            self.flip = False
        
        #makes sure the player stays on the screen
        if self.rect.left + dx < 100:
            dx =100-self.rect.left 
        if self.rect.right + dx > SCREEN_WIDTH-100:
            dx = SCREEN_WIDTH - self.rect.right -100

        #update rectangles position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x-10, self.rect.y-20))
        pygame.draw.rect(screen, WHITE, self.rect, 2)
        
