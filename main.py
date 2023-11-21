import pygame
import time
import random
pygame.font.init()


# Set Global Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 5 # Player Velocity

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "red", player)

    pygame.display.update()


def main():
    run = True
    player = pygame.Rect(
        int((WIDTH / 2) - (PLAYER_WIDTH / 2)),
        HEIGHT - PLAYER_HEIGHT - 5,
        PLAYER_WIDTH,
        PLAYER_HEIGHT,
    )
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
        if keys[pygame.K_LEFT] and (player.x-PLAYER_VEL) > 5:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and (player.x+PLAYER_VEL) < WIDTH-PLAYER_WIDTH-5:
            player.x += PLAYER_VEL

        draw(player, elapsed_time)

    pygame.quit()


if __name__ == "__main__":
    main()
