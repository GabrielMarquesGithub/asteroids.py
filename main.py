import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Verifica eventos
        for event in pygame.event.get():
            # Se o evento for de saída, encerra o programa
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)  # Atualiza o grupo de objetos atualizáveis

        screen.fill((0, 0, 0))  # Preenche a tela com preto

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # Atualiza a tela

        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                return

        # Isso pausará o loop do jogo até que 1/60 de segundo tenha passado.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
