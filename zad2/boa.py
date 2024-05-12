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
    max_iter = 100
    lb = -2.048  # lowerbound
    ub = 2.048
    dim = 20
    pop_size = 25
    c = 0.8  # są współczynnikami odpowiadającymi za regulację powyższej wartości
    a = 0.1  # i według autorów powinny być to liczby rzeczywiste w przedziale [0;1].
    pp = 0.8  # pomocą prawdopodobieństwa przełączenia
    t = 0
    but_positions = swarm_generator(lb, ub, pop_size, dim)

    while t < max_iter:
        but_fitness = np.array([objective_func(bat) for bat in but_positions])
        but_smell = np.array([c * but ** a for but in but_fitness])
        best_position = np.argmin(but_fitness)
        if t % 20 == 0:
            print("Gen:", t)
            print("Best position:", but_fitness[best_position])
        new_but_postions = np.zeros([pop_size, dim], dtype='float')
        new_but_fitness = np.zeros(pop_size, dtype='float')
        for i in range(pop_size):
            if rand() < pp:
                # global
                new_but_postions[i] = but_positions[i] + (
                            but_positions[best_position] * rand() ** 2 - but_positions[i]) * but_smell[i]
            else:
                # lokal
                parent = but_positions[i]
                possible_candidates = [candidate for candidate in range(pop_size) if candidate != i]
                j, k = but_positions[np.random.choice(possible_candidates, 2, replace=False)]
                new_but_postions[i] = but_positions[i] + (j * rand() ** 2 - k) * but_smell[i]
        but_positions = new_but_postions
        a = 0.1 + 0.2 * (t / max_iter)
        t += 1


boa()
