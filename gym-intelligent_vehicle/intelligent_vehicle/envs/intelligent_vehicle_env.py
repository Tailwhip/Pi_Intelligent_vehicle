import gym
from gym import spaces
import numpy as np
import random
from math import log

import ultrasonic as us
import intensity as int
import acceleration as acc
import servo as sv
import led


class IntelligentVehicleEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(IntelligentVehicleEnv, self).__init__()
        
        # initialise sensors
        us.setup()
        int.setup()
        sv.setup()
        acc.setup()
        led.setup()
        
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
        self.collision = 0

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
        self.us_left = us.getDistance(1);
        self.us_center_left = us.getDistance(2);
        self.us_center = us.getDistance(3);
        self.us_center_right = us.getDistance(4);
        self.us_right = us.getDistance(5);
        # acceleration sensor
        self.acc_X = acc.getAccX()
        self.acc_Y = acc.getAccY()
        # light intensity sensors
        int1 = int.getIntensity(1)
        int2 = int.getIntensity(2)
        int3 = int.getIntensity(3)
        int4 = int.getIntensity(4)
        
        if int1 <= 0:
            self.int_front_left = int1
        else:
            self.int_front_left = np.clip((log(int1, 110.0) + 1.178796054) * 2.4, 0.0, 1.0)
            
        if int2 <= 0:
            self.int_front_right = int2
        else:
            self.int_front_right = np.clip((log(int2, 110.0) + 1.178796054) * 2.4, 0.0, 1.0)
            
        if int3 <= 0:
            self.int_back_left = int3
        else:
            self.int_back_left = np.clip((log(int3, 110.0) + 1.178796054) * 2.4, 0.0, 1.0)
            
        if int4 <= 0:
            self.int_back_right = int4
        else:
            self.int_back_right = np.clip((log(int4, 110.0) + 1.178796054) * 2.4, 0.0, 1.0)

        obs = np.append(np.empty(0), [self.us_left, self.us_center_left, self.us_center,
                                      self.us_center_right, self.us_right, self.acc_X, self.acc_Y,
                                      self.int_front_left, self.int_front_right, self.int_back_left,
                                      self.int_back_right])
        self._get_intensity()
        #self._get_distance()
        return obs

# ----------------------------------------------------------------------------------------------------------------------
    def _take_action(self, action):
        self.riding = sv.ride(action[0])
        self.turning = sv.turn(action[1])

# ----------------------------------------------------------------------------------------------------------------------
    def reset(self):
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        sv.ride(-1)
        print('Go backward for a bit')
        self.collision = 0
        self.intensity_old = 0
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
                reward += 0.03
            self.intensity_old = self.intensity

        if self.intensity > 3.5:
            led.ping_green()
            led.ping_green()
            led.ping_green()
            reward = 1
            done = True

        if (self.us_left<= 0.3) or (self.us_center_left<= 0.2) or (self.us_center<= 0.2) or (self.us_center_right<= 0.2) or (self.us_right <= 0.2):
            self.collision += 1
        else:
            self.collision = 0
        
        if self.collision == 2:
            led.ping_red()
            led.ping_red()
            led.ping_red()
            reward = -1
            done = True

        # Execute one time step within the environment
        self._take_action(action)
        
        self.render()

        return obs, reward, done, {}

# ----------------------------------------------------------------------------------------------------------------------
    def render(self, mode='human', close=False):
        print('Obs: us1: {} | us2: {} | us3: {} | us4: {} | us5: {} int1: {} | int2: {} | int3: {} | int4: {} | accX: {} | accY: {}'.format(self.us_left, self.us_center_left, self.us_center, self.us_center_right, self.us_right, self.int_front_left, self.int_front_right, self.int_back_left, self.int_back_right, self.acc_X, self.acc_Y))
        #print('int1: {} | int2: {} | int3: {} | int4: {} | \n'.format(self.int_front_left, self.int_front_right, self.int_back_left, self.int_back_right))
        #print('acc1: {} | accY: {} \n'.format(self.acc_X, self.acc_Y))
        print('Collision: {} | Intensity: {} | Delta: {}'.format(self.collision, self.intensity, self.delta_intensity))