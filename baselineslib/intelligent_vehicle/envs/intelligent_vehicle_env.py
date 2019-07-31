import gym
from gym import error, spaces, utils
import numpy as np
from gym.utils import seeding

class IntelligentVehicle(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    super(IntelligentVehicle, self).__init__()

    self.action_space = spaces.Tuple(spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                     spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                     spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                     spaces.Box(low=0, high=1, shape=1, dtype=np.float32))

    self.observation_space = spaces.Tuple(spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32))

  def step(self, action):
    pass
  def reset(self):
    pass
  def render(self, mode='human', close=False):
    pass