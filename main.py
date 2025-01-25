import pygame
from constants import *
from player import Player

#initialise pygame
pygame.init()

#screen window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('platformyourtheweapon')

#set the frame rate
clock = pygame.time.Clock()
FPS = 60

#load images
bg_image = pygame.image.load('data/images/environment/background_wall.png').convert_alpha()
left_wall = pygame.image.load('data/images/environment/left_wall.png').convert_alpha()
right_wall = pygame.image.load('data/images/environment/right_wall.png').convert_alpha()

player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT-150)

run = True
while run:
    
    clock.tick(FPS)

    player.move()

    #draw background
    screen.blit(bg_image, (50,0))
    screen.blit(left_wall, (0,0))
    screen.blit(right_wall, (SCREEN_WIDTH-110 , 0))

    #draw sprites 
    player.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display window
    pygame.display.update()

pygame.quit()