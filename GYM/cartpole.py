

import gym
import random 


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self,env,epsilon = .1):
        super(RandomActionWrapper,self).__init__(env)
        self.epsilon = epsilon

    def action(self, action):
        if random.random()<self.epsilon:
            print("RANDOM : ",self.env.action_space.sample())
            return self.env.action_space.sample()
        return action
    
env = RandomActionWrapper(gym.make("CartPole-v0"))
total_reward= 0
total_steps = 0
obs = env.reset()
done = False

while True : 
    action  = env.action_space.sample()
    obs,reward,done,truncated,info= env.step(action)
    total_reward += reward
    total_steps+=1
    if done:
        break

print("No of steps%d\n Total reward %d "%(total_steps,total_reward)) 