import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

from player import Player

from Asteroids import Asteroids
from asteroidsfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0.0
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroids = pygame.sprite.Group()
    Asteroids.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()


    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000







if __name__ == "__main__":
    main()
