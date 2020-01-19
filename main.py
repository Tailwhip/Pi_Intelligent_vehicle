import gym

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.common.vec_env import SubprocVecEnv
from stable_baselines.gail import generate_expert_traj
from stable_baselines.gail import ExpertDataset
from stable_baselines import PPO2
from multiprocessing import freeze_support
import tensorflow as tf

import led
import intelligent_vehicle
import numpy as np
import expert_set_generator as ex_gen

# save np.load for "dataloader" problem resolve
#np_load_old = np.load

# modify the default parameters of np.load
#np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

ex_gen.generate()

#if __name__ == "__main__":
 #   freeze_support()
 
# Custom MLP policy of two layers of size 256 each with Leaky ReLu activation function
policy_kwargs = dict(act_fun=tf.nn.leaky_relu, net_arch=[256, 256])

dataset = ExpertDataset(expert_path='expert_intelligent_vehicle.npz', traj_limitation=1, batch_size=128)

# The algorithms require a vectorized environment to run
env = gym.make('int-v0')
env = DummyVecEnv([lambda: env])

model = PPO2("MlpPolicy", env, policy_kwargs=policy_kwargs, verbose=1)

# Retrieve the environment
env = model.get_env()

model.pretrain(dataset, n_epochs=3000)
print("Saving model...")
model.save("ppo2_intelligent_vehicle")

del model

print("Loading model...")
model = PPO2.load("ppo2_intelligent_vehicle", env=env)

for _ in range(1000):
    print("Learning...")
    model.learn(total_timesteps = 128)
    
    print("Saving model...")
    model.save("ppo2_intelligent_vehicle")
    

#print("Generating expert trajectories...")
#generate_expert_traj(model, 'expert_intelligent_vehicle_2', n_timesteps=int(128), n_episodes=10)

# restore np.load for future normal usage
#np.load = np_load_old

#print("Loading model...")
#model = PPO2.load("ppo2_intelligent_vehicle", env=env, policy=MlpPolicy)

obs = env.reset()
for i in range(1000):
    print("FREERIDEEEEEEEEEEEEEEEEEEEEEEEEEEE...")
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
env.close()
