from ws.RLAgents.C_ValueBase_WithFunctionApproximation.OffPolicy.dqn.agent_mgt import agent_mgt


def fn_execute():
    agent_mgr = agent_mgt(__file__)
    agent_mgr.fn_train()
    return agent_mgr.APP_INFO.ERROR_MESSAGE_

if __name__ == "__main__":
    print(fn_execute())