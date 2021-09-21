from ws.RLUtils.common.app_info_lib import DotDict

app_info = DotDict(
{
  "STRATEGY": "B_ValueBased.Bootstrapping.OffPolicy.qlearn",
  "ENV_NAME": "Gridworld-v1",
  "AGENT_CONFIG": "gridwell_qlearn",

  "AUTO_ARCHIVE": 1,
  "AUTO_INTERRUPT_HANDLING": 1,

  "DISPLAY": {
    "APP_NAME": "Q-learn",
    "BOARD_BLOCKERS": [  {"x": 1, "y": 2, "reward": -100},  {"x": 2, "y": 1, "reward": -100}],
    "BOARD_GOAL": {"x":2,"y":2, "reward": 100},
     "UNIT": 100,
    "WIDTH": 6,
    "HEIGHT": 5
  }
}
)

def fn_get_args():
    return app_info