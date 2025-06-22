import pygame

from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN,
    PLAYER_SHOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    SHOT_LIFETIME,
    SHOT_RADIUS,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    containers = None

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.shot_timer = 0
        self.rotation = 0

    def get_forward_vector(self):
        return pygame.Vector2(0, 1).rotate(self.rotation)

    def triangle(self):
        forward = self.get_forward_vector()
        right = self.get_forward_vector().rotate(90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shot_timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Gira para a esquerda
        if keys[pygame.K_d]:
            self.rotate(dt)  # Gira para a direita

        if keys[pygame.K_w]:
            self.move(dt)  # Move para frente
        if keys[pygame.K_s]:
            self.move(-dt)  # Move para trás

        if keys[pygame.K_SPACE]:
            self.shot()  # Dispara

    def move(self, dt):
        forward = self.get_forward_vector()
        self.position += forward * PLAYER_SPEED * dt

    def shot(self):
        if self.shot_timer > 0:
            return  # Não dispara se o tempo de recarga não tiver acabado

        self.shot_timer = PLAYER_SHOOT_COOLDOWN

        forward = self.get_forward_vector()

        shot_position = self.position + forward * (self.radius + SHOT_RADIUS + 5)

        shot = Shot(shot_position.x, shot_position.y, SHOT_LIFETIME)
        shot.velocity = forward * PLAYER_SHOT_SPEED
