import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import GAME_FPS, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from shot import Shot


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (updatable, drawable, shots)

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

            for shot in shots:
                if shot.check_collision(asteroid):
                    asteroid.kill()  # Remove o asteroide se colidir com o tiro
                    shot.kill()  # Remove o tiro após a colisão

        # Isso pausará o loop do jogo até que 1/60 de segundo tenha passado.
        dt = clock.tick(GAME_FPS) / 1000


if __name__ == "__main__":
    main()
