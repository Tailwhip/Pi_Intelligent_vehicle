import numpy as np
import os
import random

actions = np.empty((2, ), dtype=np.float16)
episode_returns = np.empty(0, dtype=np.float16)
rewards = np.empty(0, dtype=np.float16)
obs = np.empty(0, dtype=np.float16)
episode_starts = np.empty(0, dtype=np.float16)

np.savez('npzfile.npz', actions=actions, episode_returns=episode_returns, rewards=rewards,
         obs=obs, episode_starts=episode_starts)

# npzfile = np.load('npzfile.npz')

npzfile = np.load('expert_intelligent_vehicle.npz')

a = npzfile['actions']
b = npzfile['obs']
c = npzfile['episode_returns']
d = npzfile['rewards']
e = npzfile['episode_starts']

file = open('expert_intelligent_vehicle.txt')
try:

    for line in file:
        sample_buffer = []
        float_buffer = []
        for i, sign in enumerate(line):
            # change ',' into '.'
            if sign == ',':
                sign = '.'
            if sign == 'a':
                string_buffer = ''
                j = i
                while line[j] != '>':
                    j += 1
                    if line[j] == ';':
                        print('Sign: {}'.format(line[j]))
                        float_buffer.append(float(string_buffer))
                        string_buffer = ''
                        print('float_buffer: {}'.format(float_buffer))
                    else:
                        print('Sign: {}'.format(line[j]))
                        string_buffer += line[j]
                        print('string_buffer: {}'.format(string_buffer))
            sample_buffer.append(float_buffer)
        actions = np.asanyarray(sample_buffer)
        print('actions: {}'.format(actions))
finally:
    file.close()