"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count Xs and Os
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)
    # X starts first
    return "X" if x_count == o_count else "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==EMPTY:
                action_set.add((i,j))

    return action_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp_board=copy.deepcopy(board)
    temp_board[action[0]][action[1]]=player(board)

    return temp_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for mark in [X,O]:
        for i in range(len(board)):
            if all(row[i]==mark for row in board ):
                return mark
        if all(board[i][len(board)-1-i]==mark for i in range(len(board)) ):
            return mark
        if all(board[i][i]==mark for i in range(len(board)) ):
            return mark
        for row in board:
            if all(i==mark for i in row):
                return mark
    return None






def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) or all(cell!=EMPTY for row in board for cell in row):
        return True
    else:
        return False






def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0




def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def MAX_VALUE(board):
        if terminal(board):
            return utility(board)

        v=float('-inf')
        for action in actions(board):
            v=max(v,MIN_VALUE(result(board,action)))
        return v

    def MIN_VALUE(board):
        if terminal(board):
            return utility(board)

        v = float('inf')
        for action in actions(board):
            v = min(v, MAX_VALUE(result(board, action)))
        return v

    if terminal(board):
        return None

    current=player(board)
    best_move=None

    if current=='X':
        value=float('-inf')
        for action in actions(board):
            move_val=MIN_VALUE(result(board,action))
            if move_val > value:
                value = move_val
                best_move=action
    else:
        value = float('inf')
        for action in actions(board):
            move_val = MAX_VALUE(result(board, action))
            if move_val < value:
                value = move_val
                best_move = action


    return best_move
