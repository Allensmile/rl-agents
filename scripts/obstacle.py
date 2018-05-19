import gym

from rl_agents.agents.dqn.dqn_pytorch import DqnPytorchAgent
from rl_agents.agents.dqn.graphics import ValueFunctionViewer
from rl_agents.trainer.simulation import Simulation
from rl_agents.trainer.state_sampler import ObstacleStateSampler

import obstacle_env


def make_env():
    env_name = 'obstacle-v0'
    environment = gym.make(env_name)
    env_sampler = ObstacleStateSampler()
    return environment, env_sampler


def dqn_pytorch(environment):
    config = {
        "layers": [100, 100],
        "memory_capacity": 50000,
        "batch_size": 100,
        "gamma": 0.9,
        "epsilon": [1.0, 0.01],
        "epsilon_tau": 50000,
        "target_update": 1
    }
    return DqnPytorchAgent(environment, config)


if __name__ == "__main__":
    gym.logger.set_level(gym.logger.INFO)
    env, sampler = make_env()
    agent = dqn_pytorch(env)
    agent_viewer = ValueFunctionViewer(agent, sampler)
    sim = Simulation(env, agent, num_episodes=5000, agent_viewer=agent_viewer)
    sim.train()

