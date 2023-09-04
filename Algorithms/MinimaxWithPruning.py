from Evaluation.EvaluationFunction import *
from MovesGenerators.WhitesMove import *
from MovesGenerators.BlacksMove import *

def minimax_with_pruning(chessboard, depth, alpha, beta, maximizingPlayer):
    if chessboard.mate:
        return -4000 * chessboard.color, None
    if chessboard.stalemate:
        return 2000 * chessboard.color, None
    if depth == 0:
        return eval_board(chessboard), None

    best_move = None

    if maximizingPlayer:
        max_eval = -float('inf')
        chessboard.color = 1
        moves = chessboard.possible_moves_white
        for move in moves:
            chessboard.color = 1
            # Make the move
            white_turn(move[0], chessboard)

            # Recursive minimax call
            eval_score, _ = minimax_with_pruning(chessboard, depth - 1, alpha, beta, False)

            # Undo the move
            black_turn("undo", chessboard)

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move[0]

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break

        return max_eval, best_move

    else:
        min_eval = float('inf')
        chessboard.color = -1
        moves = chessboard.possible_moves_black
        for move in moves:
            chessboard.color = -1
            # Make the move
            black_turn(move[0], chessboard)

            # Recursive minimax call
            eval_score, _ = minimax_with_pruning(chessboard, depth - 1, alpha, beta, True)

            # Undo the move
            white_turn("undo", chessboard)

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move[0]

            beta = min(beta, eval_score)
            if beta <= alpha:
                break

        return min_eval, best_move
