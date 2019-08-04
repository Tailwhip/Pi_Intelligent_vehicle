import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO1

import intelligent_vehicle


# The algorithms require a vectorized environment to run
env = gym.make('int-v0')
env = DummyVecEnv([lambda: env])

model = PPO1(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=20000)
model.save("ppo1_intelligent_vehicle")

del model

model = PPO1.load("ppo1_intelligent_vehicle")

obs = env.reset()
for i in range(5000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
env.close()