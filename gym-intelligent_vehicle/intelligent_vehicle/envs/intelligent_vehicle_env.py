import gym
from gym import spaces
import numpy as np
import random
import time
from math import log
import threading
import os

import ultrasonic as us
import intensity as int
#import acceleration as acc
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
        #acc.setup()
        led.setup()
        
        self.run_counter = 1
        self.timestamp = 0
        self.delta_time = 0
        self.time_old = time.time()
        self.total_time = 0
        self.thread = threading.Thread(target = self._take_action, args=[[0,0]])
        self.thread.start()
        self.clear = lambda: os.system('clear')
        
        self.win_counter = 0
        self.collision_counter = 0
        
        # set the reward range
        # self.reward_range(0, 1)
        self.riding = 'Riding'
        self.turning = 'Turning'
        self.max_steps = 100
        self.step_counter = self.max_steps
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
        
        # collisions
        self.col_center = 0
        self.col_left = 0
        self.col_right = 0
        self.col_center_left = 0
        self.col_center_right = 0

        # turning actions space
        self.turn_left = 0
        self.turn_right = 0
        # riding actions space
        self.ride_forward = 0
        self.ride_backward = 0

        # defining an action space
        self.action_space = spaces.Box(low=-1.0, high=1.0, shape=(2, ), dtype=np.float16)

        # defining an observation space
        self.observation_space = spaces.Box(low=0.0, high=1.0, shape=(9, ), dtype=np.float16)

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
        #self.acc_X = acc.getAccX()
        #self.acc_Y = acc.getAccY()
        # light intensity sensors
        
        int1 = int.getIntensity(1)
        int2 = int.getIntensity(2)
        int3 = int.getIntensity(3)
        int4 = int.getIntensity(4)
        
        if int1 <= 0:
            self.int_front_left = 0
        else:
            self.int_front_left = round((np.clip((log(int1, 110.0) + 1.462), 0.0, 1.0)), 2)
            
        if int2 <= 0:
            self.int_front_right = 0
        else:
            self.int_front_right = round((np.clip((log(int2, 110.0) + 1.462), 0.0, 1.0)), 2)
            
        if int3 <= 0:
            self.int_back_left = 0
        else:
            self.int_back_left = round((np.clip((log(int3, 110.0) + 1.462), 0.0, 1.0)), 2)
            
        if int4 <= 0:
            self.int_back_right = 0
        else:
            self.int_back_right = round((np.clip((log(int4, 110.0) + 1.462), 0.0, 1.0)), 2)

        obs = np.append(np.empty(0), [self.us_left, self.us_center_left, self.us_center,
                                      self.us_center_right, self.us_right, self.int_front_left, self.int_front_right,
                                      self.int_back_left, self.int_back_right])
                                        #self.acc_X, self.acc_Y
        self._get_intensity()
        #self._get_distance()
        return obs

# ----------------------------------------------------------------------------------------------------------------------
    def _take_action(self, action):
        self.riding = sv.ride(action[0], action[1])
        time.sleep(0.4)

# ----------------------------------------------------------------------------------------------------------------------
    def reset(self):
        sv.stop()
        self.intensity_old = 0
        self.timestamp = 0
        self.delta_time = 0
        self.time_old = time.time()
        self.total_time = 0
        self.run_counter += 1
        #self.step_counter = self.max_steps
        
        self.col_center = 0
        self.col_left = 0
        self.col_right = 0
        self.col_center_left = 0
        self.col_center_right = 0
        return self._get_obs()

#----------------------------------------------------------------------------------------------------------------------
    def check_collision(self, col_bias, sens_value, ride_value, turn_value):
        if sens_value <= col_bias:
            self.col_center += 1
            self.col_left += 1
            self.col_right += 1
            self.col_center_left += 1
            self.col_center_right += 1
        else:
            self.col_center = 0
            self.col_left = 0
            self.col_right = 0
            self.col_center_left = 0
            self.col_center_right = 0
        
        if self.col_center or self.col_left or self.col_right or self.col_center_left or self.col_center_right == 6:
            led.ping_red()
            led.ping_red()
            reward = -1
            self.collision_counter += 1
            sv.ride(ride_value, turn_value)
            time.sleep(3)
            #sv.stop()
            done = True
            self.reset()

#----------------------------------------------------------------------------------------------------------------------
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
                reward += 0.02
            self.intensity_old = self.intensity

        if self.intensity > 3.2:
            led.ping_green()
            led.ping_green()
            led.ping_green()
            self.win_counter += 1
            sv.ride(-1, 0)
            time.sleep(5)
            sv.stop()
            reward = 1
            done = True
                
        self.check_collision(0.1, self.us_center, -1, 0)
        self.check_collision(0.1, self.us_left, -1, -1)
        self.check_collision(0.1, self.us_right, -1, 1)
        self.check_collision(0.1, self.us_center_left, -1, -0.5)
        self.check_collision(0.1, self.us_center_right, -1, 0.5)

        #self.timestamp = time.time()
        #self.deltatime = self.timestamp - self.time_old
        #self.total_time += self.deltatime
        #self.time_old = self.timestamp
        
        # Execute one time step within the environment
        self.thread.join()
        self.thread = threading.Thread(target = self._take_action, args=[action])
        self.thread.start()
                
        self.render()
        
        #self.step_counter -= 1
        #if self.step_counter == 0:
        #    sv.stop()
            
        return obs, reward, done, {}

# ----------------------------------------------------------------------------------------------------------------------
    def render(self, mode='human', close=False):
        
        
        self.clear()
        
        print('Obs: us1: {} | us2: {} | us3: {} | us4: {} | us5: {}'.format(self.us_left, self.us_center_left, self.us_center, self.us_center_right, self.us_right))
        print('int1: {} | int2: {} | int3: {} | int4: {} | \n'.format(self.int_front_left, self.int_front_right, self.int_back_left, self.int_back_right))
        #print('acc1: {} | accY: {} \n'.format(self.acc_X, self.acc_Y))
        #print('Coll_left: {} | Coll_center_left: {} | Coll_center: {} | Coll_center_right: {} | Coll_right: {} |'.format(self.col_left, self.col_center_left, self.col_center, self.col_center_right, self.col_right))
        print('Run number: {} | Collisions: {} | Wins: {} | Intensity: {} | Delta: {}'.format(self.run_counter, self.collision_counter, self.win_counter, self.intensity, self.delta_intensity))