import pygame
import time
import random

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 1 # Player Velocity


def draw(player):
    WIN.blit(BG, (0, 0))

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

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x-PLAYER_VEL) > 5:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and (player.x+PLAYER_VEL) < WIDTH-PLAYER_WIDTH-5:
            player.x += PLAYER_VEL

        draw(player)

    pygame.quit()


if __name__ == "__main__":
    main()
