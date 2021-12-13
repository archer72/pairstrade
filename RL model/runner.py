from environment import Simulator
from agent import ActorCriticAgent
import datetime as dt
import numpy as np
def main():
    actions = ["buy", "sell", "hold"]

    n_iter = 5
    for i in range(n_iter):

        env_train = Simulator(['lnt', 'es'], dt.datetime(2010, 1, 4), dt.datetime(2013, 12, 31))

        agent = ActorCriticAgent(lookback=env_train.init_state())
        #critic_agent = CriticsAgent(lookback=env.init_state())
        action = agent.init_query()


        while env_train.has_more():
        	action = actions[action] # map action from id to name
        	print "Runner: Taking action", env_train.date, action
        	reward, state = env_train.step(action)
        	action = agent.query(state, reward)

    #env_test = Simulator(['scg', 'wec'], dt.datetime(2013, 10, 18), dt.datetime(2016, 11, 30))
    env_test = Simulator(['scg', 'wec'], dt.datetime(2016, 11, 30), dt.datetime(2017, 11, 30))
    agent.reset(lookback=env_test.init_state())
    while env_test.has_more():
        action = actions[action] # map action from id to name
        print "Runner: Taking action", env_test.date, action
        reward, state = env_test.step(action)
        action = agent.query(state, reward)

if __name__ == '__main__':
    main()
