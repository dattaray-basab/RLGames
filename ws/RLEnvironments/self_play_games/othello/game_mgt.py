from __future__ import print_function

import copy
import sys
from collections import namedtuple

sys.path.append('..')

from .board_mgt import board_mgt
import numpy as np

EXISTING = True

def game_mgt(BOARD_SIZE):

    square_content = {
        -1: "X",
        +0: "-",
        +1: "O"
    }

    def fn_get_init_board():
        return np.array(board_mgt(BOARD_SIZE).fn_init_board())

    def fn_get_board_size():
        return BOARD_SIZE

    def fn_get_action_size():
        return BOARD_SIZE * BOARD_SIZE

    def fn_get_next_state(pieces, player, action):
        if action is None:
            return None
        board = board_mgt(BOARD_SIZE)
        move = (int(action / BOARD_SIZE), action % BOARD_SIZE)
        success, next_pieces = board.fn_execute_flips(pieces, move, player)
        pieces = next_pieces
        if not success:
            return pieces
        return pieces

    def fn_get_valid_moves(pieces, player):
        valid_moves = [0]*fn_get_action_size()
        b = board_mgt(BOARD_SIZE)

        legalMoves =  b.fn_find_legal_moves(pieces, player)
        if len(legalMoves)==0:
            return None
        for x, y in legalMoves:
            valid_moves[BOARD_SIZE * x + y]=1
        return np.array(valid_moves)

    def fn_get_game_progress_status(pieces, player):
        if player is None:
            return fn_game_status(pieces)

        board = board_mgt(BOARD_SIZE)

        if board.fn_are_any_legal_moves_available(pieces, player):
            return 0

        if board.fn_get_advantage_count(pieces, player) > 0:
            return 1
        return -1

    def fn_game_status(pieces):
        val = sum(pieces.flatten())
        status = 0 if val == 0 else -1 if val < 0 else 1
        return status

    def fn_get_canonical_form(pieces, player):
        canonical_pieces = copy.deepcopy(player * pieces)
        return canonical_pieces

    def fn_get_symmetric_samples(pieces, policy):
        pi_board = np.reshape(policy, (BOARD_SIZE, BOARD_SIZE))
        list_of_symetries = []

        for i in range(1, 5):
                rotated_board = np.rot90(pieces, i)
                rotated_actions_rel_to_board = np.rot90(pi_board, i)
                list_of_symetries += [(rotated_board, list(rotated_actions_rel_to_board.ravel()))]
                rotated_board_flipped = np.fliplr(rotated_board)
                rotated_actions_rel_to_board_flipped = np.fliplr(rotated_actions_rel_to_board)
                list_of_symetries += [(rotated_board_flipped, list(rotated_actions_rel_to_board_flipped.ravel()))]
        return list_of_symetries

    def fn_get_state_key(pieces):
        return pieces.tostring()

    def fn_get_score(pieces, player):
        b = board_mgt(BOARD_SIZE)
        return b.fn_get_advantage_count(pieces, player)

    def fn_display(pieces):
        n = pieces.shape[0]
        print("   ", end="")
        for y in range(n):
            print(y, end=" ")
        print("")
        print("-----------------------")
        for y in range(n):
            print(y, "|", end="")    # print the row #
            for x in range(n):
                piece = pieces[y][x]    # get the piece to print
                print(square_content[piece], end=" ")
            print("|")
        print("-----------------------")


    game_mgr = namedtuple('_', [
        'fn_get_init_board',
        'fn_get_board_size',
        'fn_get_action_size',
        'fn_get_next_state',

        'fn_get_valid_moves',
        'fn_get_game_progress_status',
        'fn_game_status',
        'fn_get_canonical_form',

        'fn_get_symmetric_samples',
        'fn_get_state_key',
        'fn_get_score' ,
        'fn_display',
        ]
    )

    game_mgr.fn_get_init_board = fn_get_init_board
    game_mgr.fn_get_board_size = fn_get_board_size
    game_mgr.fn_get_action_size = fn_get_action_size
    game_mgr.fn_get_next_state = fn_get_next_state

    game_mgr.fn_get_valid_moves = fn_get_valid_moves
    game_mgr.fn_get_game_progress_status = fn_get_game_progress_status
    game_mgr.fn_game_status = fn_game_status
    game_mgr.fn_get_canonical_form = fn_get_canonical_form

    game_mgr.fn_get_symmetric_samples = fn_get_symmetric_samples
    game_mgr.fn_get_state_key = fn_get_state_key
    game_mgr.fn_get_score = fn_get_score
    game_mgr.fn_display = fn_display

    return game_mgr