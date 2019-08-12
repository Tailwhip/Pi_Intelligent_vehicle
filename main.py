import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.gail import generate_expert_traj
from stable_baselines.gail import ExpertDataset
from stable_baselines import PPO2

import intelligent_vehicle



dataset = ExpertDataset(expert_path='expert_intelligent_vehicle.npz',
                        traj_limitation=1, batch_size=128)

# The algorithms require a vectorized environment to run
env = gym.make('int-v0')
env = DummyVecEnv([lambda: env])

model = PPO2('MlpPolicy', env, verbose=1)
model.learn(total_timesteps=2000)
model.save("ppo2_intelligent_vehicle")

generate_expert_traj(model, 'expert_intelligent_vehicle', n_timesteps=int(1500), n_episodes=3)

del model

model = PPO2.load("ppo2_intelligent_vehicle")

obs = env.reset()
for i in range(100):
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render()
env.close()