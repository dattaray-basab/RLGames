from ws.RLUtils.common.app_info_lib import DotDict

app_info = DotDict({
    'STRATEGY': 'E_SelfPlay',
    'NUM_TRAINING_ITERATIONS': 5,
    'NUM_TRAINING_EPISODES': 50,
    'NUM_OF_ITERATION_SUCCESSES_FOR_MODEL_UPGRADE': 1,
    'PROBABILITY_SPREAD_THRESHOLD': 0,
    'PASSING_SCORE': 0.5001,
    'SAMPLE_BUFFER_SIZE': 200000,
    'NUM_MC_SIMULATIONS': 25,
    'NUM_GAMES_FOR_MODEL_COMPARISON': 40,
    'EXPLORE_EXPLOIT_FACTOR': 1,

    'DO_LOAD_MODEL': True,

    'SAMPLE_HISTORY_BUFFER_SIZE': 20,

    'NUM_EPOCHS': 20,
    'BOARD_SIZE': 6,
    'NUM_TEST_GAMES': 300,

    'UCB_USE_LOG_IN_NUMERATOR': True,
    'UCB_USE_POLICY_FOR_EXPLORATION': True,

    "AUTO_ARCHIVE": 1,
    "AUTO_INTERRUPT_HANDLING": 1,
})

def fn_get_args():
    return app_info