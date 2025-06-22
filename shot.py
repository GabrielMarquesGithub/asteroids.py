import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, duration):
        super().__init__(x, y, SHOT_RADIUS)

        self.duration = duration

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, SHOT_RADIUS, 1)

    def update(self, dt):
        self.duration -= dt
        if self.duration <= 0:
            self.kill()

        self.position += self.velocity * dt
