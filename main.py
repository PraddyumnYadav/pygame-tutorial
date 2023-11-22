import pygame
import time
import random
import os

pygame.font.init()


# Set Global Variables
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 5  # Player Velocity

FONT = pygame.font.SysFont("comicsans", 30)

STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 5


def draw(player, elapsed_time, stars, highscore):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    highscore_text = FONT.render(f"Highscore: {highscore}", 1, "red")
    WIN.blit(highscore_text, ((WIDTH-highscore_text.get_width() - 10), 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

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

    star_add_increment = 2000  # miliseconds
    star_count = 0
    stars = []

    hit = False

    if "score.txt" not in os.listdir():
        f = open("score.txt", "w")
        f.write("0")
        f.close()

    while run:
        clock.tick(60)
        elapsed_time = time.time() - start_time

        with open("score.txt") as x:
            highscore = x.read()

        star_count += clock.tick(60)
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and (player.x - PLAYER_VEL) > 5:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and (player.x + PLAYER_VEL) < WIDTH - PLAYER_WIDTH - 5:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("Game Over!!", 1, "white")
            WIN.blit(
                lost_text,
                (
                    WIDTH / 2 - lost_text.get_width() / 2,
                    HEIGHT / 2 - lost_text.get_height() / 2,
                ),
            )
            pygame.display.update()
            with open("score.txt", "w") as f:
                if int(highscore) < round(elapsed_time):
                    f.write(str(round(elapsed_time)))
                else:
                    pass
            pygame.time.delay(5000)
            break

        draw(player, elapsed_time, stars, highscore)

    pygame.quit()


if __name__ == "__main__":
    main()
