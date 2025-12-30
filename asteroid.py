import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPLIT_ACCELERATION, LINE_WIDTH
from game_colors import ASTEROID_COLOR
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, ASTEROID_COLOR, self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)

        new_vector1 = self.velocity.rotate(split_angle)
        new_vector2 = self.velocity.rotate(-split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid1 = Asteroid(*self.position, new_radius)
        split_asteroid2 = Asteroid(*self.position, new_radius)

        split_asteroid1.velocity = new_vector1 * ASTEROID_SPLIT_ACCELERATION
        split_asteroid2.velocity = new_vector2 * ASTEROID_SPLIT_ACCELERATION
