import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.gail import generate_expert_traj
from stable_baselines.gail import ExpertDataset
from stable_baselines import PPO2
from multiprocessing import freeze_support

import intelligent_vehicle

if __name__ == "__main__":
    freeze_support()

    dataset = ExpertDataset(expert_path='expert_intelligent_vehicle.npz', traj_limitation=1, batch_size=128)

    # The algorithms require a vectorized environment to run
    env = gym.make('int-v0')
    env = DummyVecEnv([lambda: env])

    model = PPO2('MlpPolicy', env, verbose=1)
    model.pretrain(dataset, n_epochs=10)
    model.learn(total_timesteps=1000)
    model.save("ppo2_intelligent_vehicle")

    generate_expert_traj(model, 'expert_intelligent_vehicle', n_timesteps=int(1000), n_episodes=10)

    # remove to demonstrate saving and loading
    del model

    model = PPO2.load("ppo2_intelligent_vehicle")

    obs = env.reset()
    for i in range(100):
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
        env.render()
    env.close()
