import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.gail import generate_expert_traj
from stable_baselines.gail import ExpertDataset
from stable_baselines import PPO2
from multiprocessing import freeze_support

import led
import intelligent_vehicle
import numpy as np
import expert_set_generator as ex_gen

# save np.load for "dataloader" problem resolve
np_load_old = np.load

# modify the default parameters of np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

ex_gen.generate()

if __name__ == "__main__":
    freeze_support()

    dataset = ExpertDataset(expert_path='expert_intelligent_vehicle.npz', traj_limitation=1, batch_size=128)

    # The algorithms require a vectorized environment to run
    env = gym.make('int-v0')
    env = DummyVecEnv([lambda: env])

    model = PPO2('MlpPolicy', env, verbose=1)
    #model.pretrain(dataset, n_epochs=5000)
    #model.save("ppo2_intelligent_vehicle")
    
    #print("Loading model...")
    #model = PPO2.load("ppo2_intelligent_vehicle")
    
    for _ in range(100):
        model.learn(total_timesteps = 128)
        print("Learning...")
        model.save("ppo2_intelligent_vehicle")
        print("Saving model...")
    
    generate_expert_traj(model, 'expert_intelligent_vehicle', n_timesteps=int(128), n_episodes=10)
    print("Generating expert trajectories...")
    
    # remove to demonstrate saving and loading
    #del model
    print("Loading model...")
    model = PPO2.load("ppo2_intelligent_vehicle")

    # restore np.load for future normal usage
    np.load = np_load_old

    obs = env.reset()
    for i in range(1000):
        print("FREERIDEEEEEEEEEEEEEEEEEEEEEEEEEEE...")
        action, _states = model.predict(obs)
        obs, rewards, done, info = env.step(action)
    env.close()
