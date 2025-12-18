import pygame
import constants
from logger import log_state


def main():
    SCREEN_HEIGHT = constants.SCREEN_HEIGHT
    SCREEN_WIDTH = constants.SCREEN_WIDTH

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        log_state()
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
