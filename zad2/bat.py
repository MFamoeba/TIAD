import numpy as np
import math
from numpy.random import rand

from fun.testFunctionParameters import testFunctionParameters as tfp

def find_new_best_positions(positions_a, positions_b, objective_func):
    fitness_a = [objective_func(particle) for particle in positions_a]
    fitness_b = [objective_func(particle) for particle in positions_b]
    new_best_positions = []
    new_best_fitness = []
    for i in range(len(positions_a)):
        if fitness_a[i] < fitness_b[i]:
            new_best_positions.append(positions_a[i])
            new_best_fitness.append(fitness_a[i])
        else:
            new_best_positions.append(positions_b[i])
            new_best_fitness.append(fitness_b[i])
    return np.array(new_best_positions), np.array(new_best_fitness), np.array(fitness_b)


def objective_func(x):
    n = len(x)
    sum = 0
    for i in range(n - 1):
        sum += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2
    return sum


def swarm_generator(lb, ub, N, dim):
    X = np.zeros([N, dim], dtype='float')
    for i in range(N):
        for d in range(dim):
            X[i, d] = lb + (ub - lb) * rand()

    return X


def boundary(x, lb, ub):
    if x < lb:
        x = lb
    if x > ub:
        x = ub

    return x


def bat(testfunction=tfp.SPHERE, pop_size=150, max_iter=1000):
    # Parameters
    name, objective_func, dim, lb, ub, accuracy = testfunction.value
    a_max = 2
    a_min = 1  # min max glosnosc
    alfa = 0.8  # współczynnik alfa od 0 do 1 zmiany głośności
    r_max = 1
    r_min = 0  # min max częstosci
    gamma = 0.8  # współczynnik gamma od 0 zmiany częstosci
    f_max = 100
    f_min = 0
    t = 0
    bat_postions = swarm_generator(lb, ub, pop_size, dim)
    bat_r = np.random.uniform(r_min, r_max, pop_size)
    bat_a = np.random.uniform(a_min, a_max, pop_size)
    bat_velocity = np.zeros([pop_size, dim], dtype='float')
    bat_fitness = np.array([objective_func(bat) for bat in bat_postions])
    best_position = np.argmin(bat_fitness)
    history = [bat_fitness[best_position]]
    t += 1
    while t < max_iter:
        new_bat_postions = np.zeros([pop_size, dim], dtype='float')
        new_bat_fitness = np.zeros(pop_size, dtype='float')
        for i in range(pop_size):
            beta = rand()
            freq = f_min + (f_max - f_min) * beta

            for d in range(dim):
                # krok1
                vec1 = bat_velocity[i, d]
                vec2 = (bat_postions[i, d] - bat_postions[best_position, d]) * freq
                bat_velocity[i, d] = vec1 + vec2
                # krok2
                new_bat_postions[i, d] = bat_postions[i, d] + bat_velocity[i, d]
                new_bat_postions[i, d] = boundary(new_bat_postions[i, d], lb, ub)
            # krok3
            if rand() > bat_r[i]:
                for d in range(dim):
                    epsilon = rand() * 2 - 1
                    new_bat_postions[i, d] = bat_postions[best_position, d] + epsilon * np.mean(bat_a)
            # krok4
            new_bat_fitness[i] = objective_func(new_bat_postions[i])
            if (rand() < bat_a[i]) and (new_bat_fitness[i] < bat_fitness[best_position]):
                #print("Better by "+str(bat_fitness[i] - new_bat_fitness[i]))
                bat_a[i] = alfa * bat_a[i]
                bat_r[i] = bat_r[i] * (1 - np.exp(-gamma * t))
        # krok5

        for i in range(pop_size):
            bat_postions[i] = bat_postions[i] if bat_fitness[i] < new_bat_fitness[i] else new_bat_postions[i]

        history.append(bat_fitness[best_position])
        t += 1
    return history



