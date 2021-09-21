from ws.RLUtils.common.app_info_lib import DotDict

app_info = DotDict(
    {
        "STRATEGY": "D_PolicyGradientBased.ProximalPolicyOptimization.discrete_action",

        "NUM_EPOCHS": 4,
        "NUM_EPISODES": 20000,

        "MAX_STEPS_PER_EPISODE": 5000,

        "GAMMA": 0.99,
        "LEARNING_RATE": 0.002,

        "EPSILON": 0.1,
        "CLIPPING_LOSS_RATIO": 0.2,
        "MAX_GRADIENT_NORM": 0.5,

        "UPDATE_STEP_INTERVAL" : 2000,

        "ENV_NAME": "LunarLander-v2",

        "ACTOR_HIDDEN_LAYER_NODES": [
            {
                "LAYER_TYPE": "LINEAR",
                "NUM_NODES": 64,
                "ACTIVATION_FN": "relu"
            },
            {
                "LAYER_TYPE": "LINEAR",
                "NUM_NODES": 64,
                "ACTIVATION_FN": "relu"
            }
        ],

         "CRITIC_HIDDEN_LAYER_NODES": [
            {
                "LAYER_TYPE": "LINEAR",
                "NUM_NODES": 64,
                "ACTIVATION_FN": "relu"
            }
        ],

        "LOG_SKIP_INTERVAL": 1,
        "REWARD_GOAL": 270,
        "REWARD_CALCULATED_FROM_SINGLE_EPISODES": 0,
        "CONSECUTIVE_GOAL_HITS": 3,
        "LOG_MEAN_INTERVAL": 5,
        "MAX_RESULT_COUNT": 2,

        "AUTO_ARCHIVE": 1,
        "AUTO_INTERRUPT_HANDLING": 1,
    }
)

def fn_get_args():
    return app_info