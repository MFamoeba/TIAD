import numpy as np


def devo(population, mutation_func, objective_func, cross_function, k=1, f=0.5, max_iter=100):
    population = np.array(population)
    best_particle_history = []
    for i in range(max_iter):
        mutation_func(population, objective_func, cross_function, k, f)
        swarm_current_fitness = np.array([objective_func(particle) for particle in population])
        best_index = np.argmin(swarm_current_fitness)
        best_particle_history.append(population[best_index])
    return population, best_particle_history


def curr_k(population, objective_func, cross_function, k=1, F=0.5):
    number_of_candidates = k * 2
    pop_size = len(population)
    for j in range(pop_size):
        parent = population[j]
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates, replace=False)]
        half1, half2 = np.split(candidates, 2)
        mutant = parent + F * np.sum(half1 - half2)
        # krzyrzowanie
        child = cross_function(parent, mutant)
        population[j] = child if objective_func(child) < objective_func(parent) else parent


def best_k(population, objective_func, cross_function, k=1, F=0.5):
    number_of_candidates = k * 2
    swarm_current_fitness = np.array([objective_func(particle) for particle in population])
    best_index = np.argmin(swarm_current_fitness)
    parent = population[best_index]
    pop_size = len(population)
    for j in range(pop_size):
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates, replace=False)]
        half1, half2 = np.split(candidates, 2)
        mutant = parent + F * np.sum(half1 - half2)
        # krzyrzowanie
        child = cross_function(parent, mutant)
        population[j] = child if objective_func(child) < objective_func(parent) else parent


def bin_cross_function(parent_a, parent_b, pc=0.5):
    dims = len(parent_a)
    p = np.random.rand(dims)

    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial

#todo to nie jest expo
def exp_cross_function(parent_a, parent_b, pc=0.5, D=2):
    dims = len(parent_a)
    p = np.random.rand(dims)
    d = 1
    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial
