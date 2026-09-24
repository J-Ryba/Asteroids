
import pygame
from logger import log_event
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH


class Asteroids(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random.uniform(20, 50)
        new_v1 = self.velocity.rotate(random.uniform(20, 50))
        new_v2 = self.velocity.rotate(-random.uniform(20, 50))
        new_r = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroids(self.position.x, self.position.y, new_r)
        a2 = Asteroids(self.position.x, self.position.y, new_r)
        a1.velocity = new_v1 * 1.2
        a2.velocity = new_v2 * 1.2
