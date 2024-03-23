import numpy as np


def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))


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
