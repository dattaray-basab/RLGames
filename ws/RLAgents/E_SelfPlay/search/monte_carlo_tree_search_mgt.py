from collections import namedtuple

from ws.RLAgents.E_SelfPlay.search.policy_mgt import policy_mgt
from ws.RLAgents.E_SelfPlay.search.search_helper import search_helper


def monte_carlo_tree_search_mgt(
    app_info,
    neural_net_mgr,
    game_mgr,
):

    search_utils = search_helper(
        app_info,
        neural_net_mgr,
        game_mgr,
    )

    def fn_get_mcts_counts(state):
        for i in range(app_info.NUM_MC_SIMULATIONS):
            fn_search(state)
        state_key = game_mgr.fn_get_state_key(state)
        visit_counts = search_utils.fn_get_visit_counts(state_key)
        return visit_counts

    def fn_search(state):
        state_key = game_mgr.fn_get_state_key(state)

        s_results = search_utils.fn_get_cached_results(state)
        if s_results != 0:
            return - s_results

        state_val = search_utils.fn_visit_new_state_if_moves_remain(state)
        if state_val is not None:
            return -state_val

        # select best action at this non terminal state
        best_action = search_utils.fn_get_best_ucb_action(
            state
        )

        next_state = game_mgr.fn_get_next_state(state, player= 1, action= best_action)
        next_state_opponent_perspective = game_mgr.fn_get_canonical_form(next_state, player= -1)

        state_val_opponent_perspective = fn_search(next_state_opponent_perspective)

        search_utils.fn_expand_if_needed(state_key, best_action, state_val_opponent_perspective)

        search_utils.fn_update_state_during_backprop(state_key, best_action, state_val_opponent_perspective)

        return -state_val_opponent_perspective

    mcts_mgr = namedtuple('_', ['fn_get_policy'])

    fn_get_policy = policy_mgt(fn_get_mcts_counts)
    mcts_mgr.fn_get_policy = fn_get_policy

    return mcts_mgr

