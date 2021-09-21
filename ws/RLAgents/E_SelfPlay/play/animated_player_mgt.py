def animated_player_mgt(game_mgr):

    def fn_get_action(board):
        # fn_display(board_pieces)
        valid_moves = game_mgr.fn_get_valid_moves(board, 1)
        if valid_moves is None:
            return None
        for i in range(len(valid_moves)):
            if valid_moves[i]:
                print("[", int(i/game_mgr.fn_get_board_size()), int(i%game_mgr.fn_get_board_size()), end="] ")
        while True:
            input_move = input()
            input_coords = input_move.split(" ")
            if len(input_coords) == 2:
                try:
                    x,y = [int(i) for i in input_coords]
                    if ((0 <= x) and (x < game_mgr.fn_get_board_size()) and (0 <= y) and (y < game_mgr.fn_get_board_size())) or \
                            ((x == game_mgr.BOARD_SIZE) and (y == 0)):
                        action = game_mgr.fn_get_board_size() * x + y if x != -1 else game_mgr.fn_get_board_size() ** 2
                        if valid_moves[action]:
                            break
                except ValueError:
                    # Input needs to be an integer
                    'Invalid integer'
            print('Invalid move')
        return action
    return fn_get_action
