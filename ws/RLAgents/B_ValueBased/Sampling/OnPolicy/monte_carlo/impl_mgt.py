from ws.RLAgents.B_ValueBased.Sampling.OnPolicy.monte_carlo.montecarlo_trace_mgt import montecarlo_trace_mgt


def impl_mgt(app_info):
    Display = app_info.ENV.Display
    _fn_clear_trace, _fn_get_epsilon_greedy_action, _fn_trace_interaction, _fn_update_values_repo_from_trace = montecarlo_trace_mgt(
        app_info.ENV,
        app_info.EPSILON,
        app_info.DISCOUNT_FACTOR,
        app_info.LEARNING_RATE,
    )


    def fn_run_monte_carlo():
        _fn_clear_trace()
        for episode in range(app_info.NUM_EPISODES):
            value_table, episode_status = _fn_run_episode(Display.fn_move_cursor)
            if Display.fn_show_state_values is not None:
                Display.fn_show_state_values(value_table)
            if 'TEST_MODE' in app_info:
                if app_info.TEST_MODE: # ONLY 1 episode needed
                    break


    def _fn_run_episode(fn_move_cursor):
        new_state = None
        state = app_info.ENV.fn_reset_env()
        action = _fn_get_epsilon_greedy_action(state)

        continue_running = True
        while continue_running:
            new_state, reward, done, info = app_info.ENV.fn_take_step(action)
            continue_running = reward == 0
            _fn_trace_interaction(new_state, reward, continue_running)
            if fn_move_cursor is not None:
                fn_move_cursor(state, new_state)

            action = _fn_get_epsilon_greedy_action(new_state)

            state = new_state

        if fn_move_cursor is not None:
            fn_move_cursor(new_state)
        value_table = _fn_update_values_repo_from_trace()

        return value_table, continue_running

    return fn_run_monte_carlo
