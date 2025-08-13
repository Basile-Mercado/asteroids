import pygame
from player import Player
from asteroid import Asteroids
from asteroid_field import AsteroidField
from constants import *
from shot import Shot

def main():
    # Initialize pygame and create the main game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create sprite groups
    drawable_group = pygame.sprite.Group()
    update_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    # Assign the sprite groups to the containers of each class
    Player.containers = (drawable_group, update_group)
    Asteroids.containers = (drawable_group, update_group, asteroid_group)
    AsteroidField.containers = (update_group)
    Shot.containers = (shot_group, update_group, drawable_group)

    # Create the asteroid field and player
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # Set up the clock and frame rate
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        screen.fill((0, 0, 0))
        
        for entity in drawable_group:
            entity.draw(screen)
            
        for entity in asteroid_group:
            if entity.is_colliding(player1):
                print("Game Over!")
                pygame.quit()
                return

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
        for entity in update_group:
            entity.update(dt)


if __name__ == "__main__":
    main()
