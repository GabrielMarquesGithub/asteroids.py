import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Verifica eventos
        for event in pygame.event.get():
            # Se o evento for de saída, encerra o programa
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))  # Preenche a tela com preto
        pygame.display.flip()  # Atualiza a tela


if __name__ == "__main__":
    main()
