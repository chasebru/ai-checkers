from copy import deepcopy
import pygame
from checkers.constants import RED, WHITE

def minimax(position, depth, max_player:bool, game, draw=True, alpha=float('-inf'), beta=float('+inf')):
    if depth == 0 or position.winner() is not None:
        return position.evaluate(), position
    
    if max_player:
        value= float('-inf')
        best_move = None
        for move in get_all_moves(position, WHITE, game, draw):
            tmp, _ = minimax(move, depth-1, False, game)
            if tmp >  value:
                best_move = move
                value = tmp
            if value >= beta:
                break
            alpha = max(alpha, value)
        return value, best_move
    else:
        value= float('+inf')
        best_move = None
        for move in get_all_moves(position, RED, game, draw):
            tmp, _ = minimax(move, depth-1, True, game)
            if tmp < value:
                best_move = move
                value = tmp
            if value <= alpha:
                break
            beta = min(beta, value)
    return value, best_move
        
    
def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)
    return board
        
def get_all_moves(board, color, game, draw):
    moves = []  
    for piece in board.get_all_pieces(color):
        if draw:
            valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    return moves

def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    pygame.time.delay(0)