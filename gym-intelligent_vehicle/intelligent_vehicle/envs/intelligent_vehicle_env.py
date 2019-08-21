import gym
from gym import spaces
import numpy as np
import random

import ultrasonic as us
import intensity as int
import acceleration as acc
import servo as sv

while True:
    print("US: {} {} {} {} {} | INT: {} {} {} {} | ACC: {} {}".format(us.getDistance(1), us.getDistance(2),
    us.getDistance(3), us.getDistance(4), us.getDistance(5), int.getIntensity(1), int.getIntensity(2),
    int.getIntensity(3), int.getIntensity(4), acc.getAccX(), acc.getAccY()))
    sv.ride(0.1355)
    sv.turn(0.4658)


class IntelligentVehicleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(IntelligentVehicleEnv, self).__init__()
        
        # initialise sensors
        us.setup()
        int.setup()
        sv.setup()
        acc.setup()
        
        # set the reward range
        # self.reward_range(0, 1)

        self.riding = 'Riding'
        self.turning = 'Turning'

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
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2, ), dtype=np.float16)

        # defining an observation space
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(11, ), dtype=np.float16)

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
        self.riding = 'Ride: {}'.format(action[0])
        self.turning = 'Turn: {}'.format(action[1])

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
        print('An action is: {}'.format(self.riding))
        print('An action is: {}'.format(self.turning))
