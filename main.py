import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Block")

background = pygame.transform.scale(pygame.image.load("background.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time):
    WINDOW.blit(background, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WINDOW.blit(time_text, (10, 10))
    pygame.draw.rect(WINDOW, "red", player)

    pygame.display.update()

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        
        draw(player, elapsed_time)
    
    pygame.quit()

if __name__ == "__main__":
    main()