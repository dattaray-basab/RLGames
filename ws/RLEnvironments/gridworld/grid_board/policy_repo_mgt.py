from collections import namedtuple

def policy_table_mgt(width, height, action_size):
    init_policy = [1/ action_size] * action_size # [.25, .25, .25, .25]
    _policy_table = [[init_policy] * width for _ in range(height)]
    pass

    def fn_reset():
        nonlocal _policy_table
        _policy_table = [[init_policy] * width for _ in range(height)]

    def fn_get_policy_state_value(state):
        return _policy_table[state[1]][state[0]]

    def fn_set_policy_state_value(state, value):
        nonlocal _policy_table
        _policy_table[state[1]][state[0]] = value

    def fn_fetch_policy_table():
        return _policy_table

    ret_obj = namedtuple('_', [
        'fn_reset',
        'fn_get_policy_state_value',
        'fn_set_policy_state_value',
        'fn_fetch_policy_table',
    ])
    ret_obj.fn_reset = fn_reset
    ret_obj.fn_get_policy_state_value = fn_get_policy_state_value
    ret_obj.fn_set_policy_state_value = fn_set_policy_state_value
    ret_obj.fn_fetch_policy_table = fn_fetch_policy_table

    return ret_obj