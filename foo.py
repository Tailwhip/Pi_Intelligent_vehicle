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
b = npzfile['episode_returns']
c = npzfile['rewards']
d = npzfile['obs']
e = npzfile['episode_starts']

# print(a)


# a function to convert. As an input:
# ('string' sign_to_look_for, 'string' an_iterating_sign, 'int' iterator, '[]' buffer)
def convert(_type, _sign, _iterator, _buffer):
    string_buffer = ''
    float_buffer = []
    if _sign == _type:
        j = _iterator
        # till sign is not a '>' do...
        while line[j] != '>':
            j += 1
            # if sign is ';' then it's the end of value and it needs to be put into the float buffer
            if line[j] == ';':
                # print('Sign: {}'.format(line[j]))
                float_buffer.append(float(string_buffer))
                string_buffer = ''
                # print('float_buffer: {}'.format(float_buffer))
            # if sign is not ';' then put it into the string buffer to complete a value
            else:
                # print('Sign: {}'.format(line[j]))
                string_buffer += line[j]
                # print('string_buffer: {}'.format(string_buffer))
    # at finish put the buffer into the
    _buffer.append(float_buffer)
    return _buffer


file = open('expert_intelligent_vehicle.txt')
try:
    for line in file:
        actions_buffer = []
        episode_returns_buffer = []
        rewards_buffer = []
        obs_buffer = []
        episode_starts_buffer = []

        for i, sign in enumerate(line):
            # change ',' into '.'
            if sign == ',':
                sign = '.'
            actions_buffer = convert('a', sign, i, actions_buffer)
            '''
            # convert actions vector
            if sign == 'a':
                string_buffer = ''
                float_buffer = []
                j = i
                # till sign is not a '>' do...
                while line[j] != '>':
                    j += 1
                    # if sign is ';' then it's the end of value and it needs to be put into the float buffer
                    if line[j] == ';':
                        #print('Sign: {}'.format(line[j]))
                        float_buffer.append(float(string_buffer))
                        string_buffer = ''
                        #print('float_buffer: {}'.format(float_buffer))
                    # if sign is not ';' then put it into the string buffer to complete a value
                    else:
                        #print('Sign: {}'.format(line[j]))
                        string_buffer += line[j]
                        #print('string_buffer: {}'.format(string_buffer))
            # at finish put the buffer into the
            actions_buffer.append(float_buffer)
            
            # convert reward value
            if sign == 'r':
                string_buffer = ''
                j = i
                while line[j] != '>':
                    j += 1
            '''

        # convert buffers into np arrays
        actions = np.asanyarray(actions_buffer)
        print('actions: {}'.format(actions))
finally:
    file.close()



