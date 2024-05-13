import numpy as np
import matplotlib.pyplot as plt

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


def boa_na3(testfunction=tfp.SPHERE, pop_size=150, max_iter=1000):
    # Parameters
    name, objective_func, dim, lb, ub, accuracy = testfunction.value
    c = 1  # są współczynnikami odpowiadającymi za regulację powyższej wartości
    a = 0.1  # i według autorów powinny być to liczby rzeczywiste w przedziale [0;1].
    pp = 0.8  # pomocą prawdopodobieństwa przełączenia
    t = 0
    but_positions = swarm_generator(lb, ub, pop_size, dim)
    history = []
    but_fitness = np.array([objective_func(bat) for bat in but_positions])
    while t < max_iter:
        but_smell = np.array([c * but ** a for but in but_fitness])
        best_position = np.argmin(but_fitness)
        history.append(but_fitness[best_position])
        new_but_postions = np.zeros([pop_size, dim], dtype='float')
        new_but_fitness = np.zeros(pop_size, dtype='float')
        for i in range(pop_size):
            parent = but_positions[i]
            if rand() < pp:
                # global
                diff = but_positions[best_position] * rand() ** 2 - parent
                new_but_postions[i] = parent + diff * but_smell[i]
            else:
                # lokal
                possible_candidates = [candidate for candidate in range(pop_size) if candidate != i]
                j, k = but_positions[np.random.choice(possible_candidates, 2, replace=False)]
                diff = j * rand() ** 2 - k
                new_but_postions[i] = parent + diff * but_smell[i]
            for d in range(dim):
                new_but_postions[i, d] = boundary(new_but_postions[i, d], lb, ub)
        but_positions, but_fitness, new_but_fitness = find_new_best_positions(but_positions, new_but_postions, objective_func)
        c = 1 - 0.6 * np.sqrt(t / max_iter)
        a = 0.1 + 0.2 * (t / max_iter)
        t += 1
    return history


