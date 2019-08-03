import gym
from gym import error, spaces, utils
import numpy as np
from gym.utils import seeding
import random


class IntelligentVehicle(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(IntelligentVehicle, self).__init__()

        # set the reward range
        self.reward_range(0, 1)

        self.taken_action = 'Nothing'

        # distance sensors
        self.us_left = 0
        self.us_center_left = 0
        self.us_center = 0
        self.us_center_right = 0
        self.us_right = 0
        # acceleration sensor
        self.acc_X = 0
        self.acc_Y = 0
        # light intensity sensors
        self.int_front_left = 0
        self.int_front_right = 0
        self.int_back_left = 0
        self.int_back_right = 0

        # variables for counting the reward and finish the sequence
        self.intensity = 0
        self.delta_intensity = 0
        self.intensity_old = 0
        self.distance = 0
        self.delta_counter = 1

        # turning actions space
        self.turn_left = 0
        self.turn_right = 0
        # riding actions space
        self.ride_forward = 0
        self.ride_backward = 0

        # defining an action space
        self.action_space = spaces.Tuple((spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                          spaces.Box(low=0, high=1, shape=1, dtype=np.float32)))

        # defining an observation space
        self.observation_space = spaces.Tuple((spaces.Box(low=1, high=0, shape=1, dtype=np.float32),
                                               spaces.Box(low=1, high=0, shape=1, dtype=np.float32),
                                               spaces.Box(low=1, high=0, shape=1, dtype=np.float32),
                                               spaces.Box(low=1, high=0, shape=1, dtype=np.float32),
                                               spaces.Box(low=1, high=0, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32),
                                               spaces.Box(low=0, high=1, shape=1, dtype=np.float32)))

    # ----------------------------------------------------------------------------------------------------------------------
    def _get_intensity(self):
        self.intensity = self.int_front_left + self.int_front_right + self.int_back_left + self.int_back_right

    # ----------------------------------------------------------------------------------------------------------------------
    def _get_distance(self):
        self.distance = self.us_left + self.us_center_left + self.us_center + self.us_center_right + self.us_right

    # ----------------------------------------------------------------------------------------------------------------------
    def _get_obs(self):
        # distance sensors
        self.us_left = random.uniform(0, 1)
        self.us_center_left = random.uniform(0, 1)
        self.us_center = random.uniform(0, 1)
        self.us_center_right = random.uniform(0, 1)
        self.us_right = random.uniform(0, 1)
        # acceleration sensor
        self.acc_X = random.uniform(0, 1)
        self.acc_Y = random.uniform(0, 1)
        # light intensity sensors
        self.int_front_left = random.uniform(0, 1)
        self.int_front_right = random.uniform(0, 1)
        self.int_back_left = random.uniform(0, 1)
        self.int_back_right = random.uniform(0, 1)

        obs = np.append(np.empty(0), [self.us_left, self.us_center_left, self.us_center,
                                      self.us_center_right, self.us_right, self.acc_X, self.acc_Y,
                                      self.int_front_left, self.int_front_right, self.int_back_left,
                                      self.int_back_right])
        self._get_intensity()
        self._get_distance()
        return obs

    # ----------------------------------------------------------------------------------------------------------------------
    def _take_action(self, action):
        if (action[0] > action[1]) and (action[0] > action[2]) and (action[0] > action[3]):
            self.taken_action = 'ride forward'
        elif (action[1] > action[0]) and (action[1] > action[2]) and (action[1] > action[3]):
            self.taken_action = 'ride backward'
        elif (action[2] > action[0]) and (action[2] > action[2]) and (action[2] > action[3]):
            self.taken_action = 'turn right'
        elif (action[3] > action[0]) and (action[3] > action[2]) and (action[3] > action[3]):
            self.taken_action = 'turn left'

    # ----------------------------------------------------------------------------------------------------------------------
    def reset(self):
        print('Go backward for a bit')
        return self._get_obs()

    # ----------------------------------------------------------------------------------------------------------------------
    def step(self, action):
        obs = self._get_obs()
        reward = 0
        done = False

        self.delta_counter -= 1
        if self.delta_counter == 0:
            self.delta_counter = 1
            self.delta_intensity = self.intensity - self.intensity_old
            if self.delta_intensity <= 0.01:
                reward -= 0.05
            else:
                reward += 0.05
                self.intensity_old = self.intensity

        if self.intensity > 3.5:
            reward = 1
            done = True

        if self.distance < 0.5:
            reward = -1
            done = True

        # Execute one time step within the environment
        self._take_action(action)

        return obs, reward, done, {}

    # ----------------------------------------------------------------------------------------------------------------------
    def render(self, mode='human', close=False):
        print('Observations: {}'.format(self.us_left))
        print('An action is: {}'.format(self.taken_action))
