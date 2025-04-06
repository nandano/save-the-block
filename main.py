import pygame
import time
import random

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Block")

background = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))

def draw():
    WINDOW.blit(background, (0, 0))
    pygame.display.update()

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        draw()
    
    pygame.quit()

if __name__ == "__main__":
    main()