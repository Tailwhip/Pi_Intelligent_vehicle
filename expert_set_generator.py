import numpy as np
import os
import random

def generate():
    if os.path.isfile("expert_intelligent_vehicle.npz"):
        print("Expert trajectories already exists!")
    else:
        print("Generating expert trajectories...")
        make_npz()
        
def make_npz():
    
    actions = np.empty(0, dtype=np.float16)
    episode_returns = np.empty(0, dtype=np.float16)
    rewards = np.empty(0, dtype=np.float16)
    obs = np.empty(0, dtype=np.float16)
    episode_starts = np.empty(0, dtype=np.float16)
    
    
    # Change all ',' for '.' in training set
    # Read in the file
    with open('expert_intelligent_vehicle.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(',', '.')

    # Write the file
    with open('expert_intelligent_vehicle.txt', 'w') as file:
        file.write(filedata)


    file = open('expert_intelligent_vehicle.txt')
    try:
        actions_buffer = []
        episode_returns_buffer = []
        rewards_buffer = []
        obs_buffer = []
        episode_starts_buffer = []

        for line in file:
            for i, sign in enumerate(line):
                if sign == 'a':
                    actions_buffer.append(convert(sign, i, line))
                if sign == 'r':
                    rewards_buffer.append(convert(sign, i, line))
                if sign == 'o':
                    obs_buffer.append(convert(sign, i, line))
                if sign == 't':
                    episode_starts_buffer.append(convert(sign, i, line))
                if sign == 'e':
                    episode_returns_buffer.append(convert(sign, i, line))

        # if episode has not ended in step remove the value of total reward
        # also change the shape of the episode_returns array
        # create a temporary buffer
        buffer = []
        for i, value in enumerate(episode_returns_buffer):
            if episode_starts_buffer[i] == [1.0]:
                buffer.append(value[0])
        # rewrite episode returns with the temporary buffer
        episode_returns_buffer = buffer

        # parse episode_starts_buffer into bool
        # create a temporary buffer
        buffer = []
        for i, value in enumerate(episode_starts_buffer):
            if episode_starts_buffer[i] == [1.0]:
                buffer.append(True)
            else:
                buffer.append(False)
        # rewrite episode returns with the temporary buffer
        episode_starts_buffer = buffer

        # convert buffers into np arrays
        actions = np.asarray(actions_buffer)
        episode_returns = np.asarray(episode_returns_buffer)
        rewards = np.asarray(rewards_buffer)
        obs = np.asarray(obs_buffer)
        episode_starts = np.asarray(episode_starts_buffer)

        # print('actions: {}'.format(actions))
        # print('episode_returns: {}'.format(episode_returns))
        # print('rewards: {}'.format(rewards))
        # print('obs: {}'.format(obs))
        # print('episode_starts: {}'.format(episode_starts))
    finally:
        file.close()

        np.savez('expert_intelligent_vehicle.npz', actions=actions, obs=obs, rewards=rewards,
                 episode_returns=episode_returns, episode_starts=episode_starts)

        npzfile = np.load('expert_intelligent_vehicle.npz')

        a = npzfile['actions']
        e = npzfile['episode_returns']
        r = npzfile['rewards']
        o = npzfile['obs']
        t = npzfile['episode_starts']
        
        print("Expert trajectories .npz file generating compete")

    '''
        npzfile = np.load('expert_intelligent_vehicle-specimen.npz')

        a = npzfile['actions']
        e = npzfile['episode_returns']
        r = npzfile['rewards']
        o = npzfile['obs']
        t = npzfile['episode_starts']

        # print('actions2: \n {} \n {} \n {} '.format(a, np.shape(a), np.size(a)))
        # print('episode_returns2: \n {} \n {} \n {} '.format(e, np.shape(e), np.size(e)))
        # print('rewards2: \n {} \n {} \n {} '.format(r, np.shape(r), np.size(r)))
        # print('obs2: \n {} \n {} \n {} '.format(o, np.shape(o), np.size(o)))
        # print('episode_starts2: \n {} \n {} \n {} '.format(t, np.shape(t), np.size(t)))

        #for k in npzfile.iterkeys():
         #   print(k)
    '''

# a function to convert. As an input:
# ('string' sign_to_look_for, 'int' iterator, '[]' line of data)
def convert(_sign, _iterator, _line):
    string_buffer = ''
    float_buffer = []
    j = _iterator
    # till sign is not a '>' do...
    while _line[j] != '>':
        j += 1
        # if sign is ';' then it's the end of value and it needs to be put into the float buffer
        if _line[j] == ';':
            float_buffer.append(float(string_buffer))
            string_buffer = ''
        # if sign is not ';' then put it into the string buffer to complete a value
        else:
            string_buffer += _line[j]

    return float_buffer