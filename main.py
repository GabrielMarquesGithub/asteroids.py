import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Verifica eventos
        for event in pygame.event.get():
            # Se o evento for de saída, encerra o programa
            if event.type == pygame.QUIT:
                return

        player.update(dt)  # Atualiza o jogador

        screen.fill((0, 0, 0))  # Preenche a tela com preto
        player.draw(screen)  # Desenha o jogador

        pygame.display.flip()  # Atualiza a tela

        # Isso pausará o loop do jogo até que 1/60 de segundo tenha passado.
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
