import pygame
from circleshape import CircleShape
from game_colors import ASTEROID_COLOR
from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
