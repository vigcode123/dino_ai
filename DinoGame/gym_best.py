import pickle
from neat import nn, population, statistics, parallel
import numpy as np
import gymnasium as gym

gym.register(
        id='DinosaurGame-v0',
        entry_point='game:DinosaurGame'
    )
env = gym.make('DinosaurGame-v0')

def simulate_species(net, env, episodes=1, steps=5000, render=False):
    fitnesses = []
    for runs in range(episodes):
        inputs = env.reset()
        cum_reward = 0.0
        for j in range(steps):
            outputs = net.serial_activate(inputs)
            action = np.argmax(outputs)
            inputs, reward, done, _ = env.step(action)
            if render:
                env.render()
            if done:
                break
            cum_reward += reward

        fitnesses.append(cum_reward)

    fitness = np.array(fitnesses).mean()
    print("Species fitness: %s" % str(fitness))
    return fitness

with open('./DinoGame/model/winner.pkl', 'rb') as output:
    winner = pickle.load(output)


winner_net = nn.create_feed_forward_phenotype(winner)
simulate_species(winner_net, env, 1, 1000, render=True)
