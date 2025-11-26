import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ai-Checkers")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    pygame.init()
    board = Board()
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()