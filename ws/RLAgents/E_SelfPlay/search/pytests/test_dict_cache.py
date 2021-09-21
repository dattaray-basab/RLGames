import pytest

# from ws.RLAgents.self_play.alpha_zero.search.recursive.cache_mgt import cache_mgt
from ws.RLAgents.E_SelfPlay.search.cache_mgt import cache_mgt


def test_fn_get_state():
    dict = cache_mgt()
    dict.fn_set_data('k1', {'y1': 1, 'y2': 2})
    val = dict.fn_get_data('k1')
    assert val == {'y1': 1, 'y2': 2}
    pass

def test_fn_get_state_2():
    dict = cache_mgt()
    dict.fn_set_data('k1', {'y1': 1, 'y2': 2})

    dict.fn_set_data('k1', {'y1': 11})
    val = dict.fn_get_data('k1')
    assert val == {'y1': 11, 'y2': 2}
    pass

def test_fn_get_state_3():
    dict = cache_mgt()
    dict.fn_set_data('k1', 5)
    val = dict.fn_get_data('k1')
    assert val == 5
    pass


def test_fn_does_attr_key_exist():
    dict = cache_mgt()
    dict.fn_set_data('k1', {'y1': 1, 'y2': 2})
    attr_exists = dict.fn_does_attr_key_exist('k1', 'y1')
    assert attr_exists == True
    attr_exists = dict.fn_does_attr_key_exist('k1_not', 'y1')
    assert attr_exists == False
    attr_exists = dict.fn_does_attr_key_exist('k1', 'y1_not')
    assert attr_exists == False
    attr_exists = dict.fn_does_attr_key_exist('k1_not', 'y1_not')
    assert attr_exists == False
    pass

def test_fn_get_attr_data():
    dict = cache_mgt()
    dict.fn_set_data('k1', {'y1': 1, 'y2': '2'})
    val = dict.fn_get_attr_data('k1', 'y1')
    assert val == 1
    val = dict.fn_get_attr_data('k1', 'y2')
    assert val == '2'
    val = dict.fn_get_attr_data('k1_not', 'y2')
    assert val ==  None
    val = dict.fn_get_attr_data('k1', 'y2_not')
    assert val ==  None
    val = dict.fn_get_attr_data('k1_not', 'y2_not')
    assert val ==  None
    pass

def test_fn_set_attr_data():
    dict = cache_mgt()

    dict.fn_set_attr_data('k1', 'y1',  1)
    dict.fn_set_attr_data('k1', 'y2',  '2')

    val_1 = dict.fn_get_attr_data('k1', 'y1')
    assert val_1 == 1
    val_2 = dict.fn_get_attr_data('k1', 'y2')
    assert val_2 == '2'

    dict.fn_set_attr_data('k1', 'y2',  -222.97)
    val_2 = dict.fn_get_attr_data('k1', 'y2')
    assert val_2 == -222.97

    val = dict.fn_get_attr_data('k1_not', 'y2')
    assert val == None

    val = dict.fn_get_attr_data('k1', 'y2_not')
    assert val == None

    val = dict.fn_get_attr_data('k1_not', 'y2_not')
    assert val == None
    pass

def test_fn_incr_attr_int():
    dict = cache_mgt()

    dict.fn_set_attr_data('k1', 'y1',  1)
    dict.fn_incr_attr_int('k1', 'y1')
    val = dict.fn_get_attr_data('k1', 'y1')
    assert val == 2

    dict.fn_set_attr_data('k1', 'y1',  '1')
    dict.fn_incr_attr_int('k1', 'y1')
    val = dict.fn_get_attr_data('k1', 'y1')
    assert val == 1

    dict.fn_incr_attr_int('k1_not', 'y1')
    val = dict.fn_get_attr_data('k1_not', 'y1')
    assert val == 1

    dict.fn_incr_attr_int('k1', 'y1_not')
    val = dict.fn_get_attr_data('k1_not', 'y1')
    assert val == 1

    dict.fn_incr_attr_int('k1_not', 'y1_not')
    val = dict.fn_get_attr_data('k1_not', 'y1')
    assert val == 1