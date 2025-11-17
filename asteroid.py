from circleshape import CircleShape
import pygame
import random
from logger import log_event
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        new_angle = random.uniform(20,50)
        
        ast1 = self.velocity.copy().rotate(new_angle)
        ast2 = self.velocity.copy().rotate(-new_angle)

        v1 = ast1 * 1.2
        v2 = ast2 * 1.2

        new_rad = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid1.velocity = v1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_rad)
        asteroid2.velocity = v2

