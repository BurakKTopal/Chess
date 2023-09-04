from Evaluation.EvaluationFunction import *
from Evaluation.ZobristHashing import *
from MovesGenerators.WhitesMove import *
from MovesGenerators.BlacksMove import *

def minimax_with_zobrist_hashing_and_pruning(chessboard, depth, alpha, beta, maximizingPlayer):
    # # calculating the zobrist hash:
    zhash = zobrist_hash(chessboard)
    #
    # # searching hash in transposition table of the chessboard
    if zhash in chessboard.transposition_table:
        chessboard.counting += 1
        eval, best_move, stored_alpha, stored_beta = chessboard.transposition_table[zhash]

        # Use the stored alpha and beta if they're more restrictive.
        alpha = max(alpha, stored_alpha)
        beta = min(beta, stored_beta)

        if alpha >= beta:
            return eval, best_move

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
            eval_score, _ = minimax_with_zobrist_hashing_and_pruning(chessboard, depth - 1, alpha, beta, False)

            # Undo the move
            black_turn("undo", chessboard)

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move[0]

            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break

        chessboard.transposition_table[zhash] = (max_eval, best_move, alpha, beta)
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
            eval_score, _ = minimax_with_zobrist_hashing_and_pruning(chessboard, depth - 1, alpha, beta, True)

            # Undo the move
            white_turn("undo", chessboard)

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move[0]

            beta = min(beta, eval_score)
            if beta <= alpha:
                break

        chessboard.transposition_table[zhash] = (min_eval, best_move, alpha, beta)
        return min_eval, best_move