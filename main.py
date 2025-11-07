import pygame
from checkers.constants import WIDTH, HEIGHT

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ai-Checkers")

def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

    pygame.quit()

if __name__ == "__main__":
    main()