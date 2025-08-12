import pygame
import player
from constants import *

def main():
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill((0, 0, 0))
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        player1.update(dt)


if __name__ == "__main__":
    main()
