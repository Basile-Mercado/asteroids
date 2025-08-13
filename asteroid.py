from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 1)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_radius = random.uniform(20, 50)
        
        vec1 = self.velocity.rotate(random_radius)
        vec2 = self.velocity.rotate(-random_radius)
        
        ast1 = Asteroids(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        ast2 = Asteroids(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        
        ast1.velocity = vec1 * 1.2
        ast2.velocity = vec2 * 1.2