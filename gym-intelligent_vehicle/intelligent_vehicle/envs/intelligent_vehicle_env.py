import gym
from gym import spaces
from gym.utils import EzPickle
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


class IntelligentVehicleEnv(gym.Env, EzPickle):
    metadata = {'render.modes': ['human']}

    def __init__(self):
        super(IntelligentVehicleEnv, self).__init__()
        
        EzPickle.__init__(self)
        
        # initialise sensors
        us.setup()
        int.setup()
        sv.setup()
        #acc.setup()
        led.setup()
        
        self.run_counter = 0
        # a variables for meassuring one frame time:
        '''
        self.timestamp = 0 
        self.delta_time = 0
        self.time_old = time.time()
        self.total_time = 0
        '''
        self.thread = threading.Thread(target = self._take_action, args = [[0,0]])
        self.thread.start()
        self.clear = lambda: os.system('clear')
        
        # variables for counting mean reward
        self.total_reward = 0
        self.total_steps = 0  # total steps count
        self.step_counter = 0  # the number of step in the current sequence
        self.mean_reward = 0
        
        # variables for research purpose
        self.win_counter = 0
        self.collision_counter = 0
        self.action = [0, 0]
        
        # set the reward range
        self.riding = 'Riding'
        self.turning = 'Turning'
        self.max_steps = 100
        self.step_counter = 0
        
        # distance sensors
        self.us_left = 0
        self.us_center_left = 0
        self.us_center = 0
        self.us_center_right = 0
        self.us_right = 0
        self.col_count_bias = 2
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

        # defining an action space
        self.action_space = spaces.Box(low = -1.0, high = 1.0, shape = (2, ), dtype = np.float16)

        # defining an observation space
        self.observation_space = spaces.Box(low = 0.0, high=1.0, shape = (9, ), dtype = np.float16)
# ----------------------------------------------------------------------------------------------------------------------
    def _sum_intensity(self):
        self.intensity = self.int_front_left + self.int_front_right + self.int_back_left + self.int_back_right

# ----------------------------------------------------------------------------------------------------------------------
    def _get_obs(self):
        # distance sensors
        self.us_left = round(us.getDistance(1), 2)
        self.us_center_left = round(us.getDistance(2), 2)
        self.us_center = round(us.getDistance(3), 2)
        self.us_center_right = round(us.getDistance(4), 2)
        self.us_right = round(us.getDistance(5), 2)
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
        self._sum_intensity()
        return obs

# ----------------------------------------------------------------------------------------------------------------------
    def _take_action(self, action):
        self.riding = sv.ride(action[0], action[1])
        #self.action[0] = action[0]
        #self.action[1] = action[1]
        time.sleep(0.4)

# ----------------------------------------------------------------------------------------------------------------------
    def _write_report(self):
        with open('Report.txt', 'a+') as file:                
            filedata = file.write('\nSummary: {} | Step: {} | Reward: {}'.format(self.run_counter, self.total_steps, self.total_reward))
        file.close()
        
# ----------------------------------------------------------------------------------------------------------------------
    def reset(self):
        sv.stop()
        self.total_steps += self.step_counter
        '''
        if self.delta_frames > 0:
            self.mean_reward = self.total_reward / self.delta_frames
        else:
            self.mean_reward = 0
        '''
        #print('Summary: {} | Step: {} | Reward: {}'.format(self.run_counter, self.total_steps, self.total_reward))
        self._write_report()
        self.intensity_old = 0
        #self.timestamp = 0
        #self.delta_time = 0
        #self.time_old = time.time()
        #self.total_time = 0
        self.run_counter += 1
        self.total_reward = 0
        self.mean_reward = 0
        self.step_counter = 0
        
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
            
        self.render()
        
        if self.col_center == self.col_count_bias or self.col_left == self.col_count_bias or self.col_right == self.col_count_bias or self.col_center_left == self.col_count_bias or self.col_center_right == self.col_count_bias:
            sv.stop()
            led.ping_red()
            led.ping_red()
            led.ping_red()           
            self.collision_counter += 1
            #sv.ride(ride_value, turn_value)
            time.sleep(3)
            return -1, True
        else:
            return 0, False

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
            sv.stop()
            led.ping_green()
            led.ping_green()
            led.ping_green()
            self.win_counter += 1
            #sv.ride(-1, 0)
            time.sleep(3)
            reward = 1
            done = True

        # chcecking collisions:
        if not done:
            check_collision = self.check_collision(0.1, self.us_center, -1, 0)
            reward += check_collision[0]
            done = check_collision[1]
        
        if not done:
            check_collision = self.check_collision(0.1, self.us_left, -1, -1)
            reward += check_collision[0]
            done = check_collision[1]
        
        if not done:
            check_collision = self.check_collision(0.1, self.us_right, -1, 1)
            reward += check_collision[0]
            done = check_collision[1]
        
        if not done:
            check_collision = self.check_collision(0.1, self.us_center_left, -1, -0.5)
            reward += check_collision[0]
            done = check_collision[1]
        
        if not done:
            check_collision = self.check_collision(0.1, self.us_center_right, -1, 0.5)
            reward += check_collision[0]
            done = check_collision[1]
        
        '''
        # Meassuring the one frame time for multithreading purpose:
        self.timestamp = time.time()
        self.deltatime = self.timestamp - self.time_old
        self.total_time += self.deltatime
        self.time_old = self.timestamp
        '''
        
        # Execute one time step within the environment
        self.thread.join()
        self.thread = threading.Thread(target = self._take_action, args = [action])
        self.thread.start()
        
        self.step_counter += 1
        
        self.total_reward += reward
        
        return obs, reward, done, {}

# ----------------------------------------------------------------------------------------------------------------------
    def render(self, mode = 'human', close = False):
        self.clear()
        print('Obs: us1: {} | us2: {} | us3: {} | us4: {} | us5: {}'.format(self.us_left, self.us_center_left, self.us_center, self.us_center_right, self.us_right))
        print('int1: {} | int2: {} | int3: {} | int4: {} | \n'.format(self.int_front_left, self.int_front_right, self.int_back_left, self.int_back_right))
        #print('acc1: {} | accY: {} \n'.format(self.acc_X, self.acc_Y))
        print('Coll_left: {} | Coll_center_left: {} | Coll_center: {} | Coll_center_right: {} | Coll_right: {} |'.format(self.col_left, self.col_center_left, self.col_center, self.col_center_right, self.col_right))
        #print('Run number: {} | Collisions: {} | Wins: {} | Intensity: {} | Delta: {}'.format(self.run_counter, self.collision_counter, self.win_counter, self.intensity, self.delta_intensity))       
        #print('Step counter: {} | Ride: {} | Turn: {}'.format(self.step_counter, self.action[0], self.action[1]))
        #pass