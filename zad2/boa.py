import numpy as np
from numpy.random import rand
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

def boa():
    # Parameters
    lb = -2.048 # lowerbound
    ub = 2.048
    dim = 20
    pop_size = 250