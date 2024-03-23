import numpy as np

from Zad1.algo.tools import find_new_best_positions


def devo(population, mutation_func, objective_func, cross_function, k=1, f=0.5, max_iter=100):
    population = np.array(population)
    best_particle_history = []
    for i in range(max_iter):
        #robienie dziecie
        child_positions = mutation_func(population, objective_func, cross_function, k, f)
        #selekcja
        population, swarm_current_fitness = find_new_best_positions(population, child_positions, objective_func)
        best_index = np.argmin(swarm_current_fitness)
        best_particle_history.append(population[best_index])
    return population, best_particle_history


def curr_k(population, objective_func, cross_function, k=1, F=0.5):
    number_of_candidates = k * 2
    pop_size = len(population)
    child_positions = []
    for j in range(pop_size):
        parent = population[j]
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates, replace=False)]
        half1, half2 = np.split(candidates, 2)
        mutant = parent + F * np.sum(half1 - half2)
        # krzyrzowanie
        child_positions.append(cross_function(parent, mutant))
    return child_positions


def curr_to_best_k(population, objective_func, cross_function, k=1, F=0.5, delta=0.5):
    number_of_candidates = k * 2
    pop_size = len(population)
    swarm_current_fitness = np.array([objective_func(particle) for particle in population])
    best_index = np.argmin(swarm_current_fitness)
    best_parent = population[best_index]
    child_positions = []
    for j in range(pop_size):
        current_parent = population[j]
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates, replace=False)]
        half1, half2 = np.split(candidates, 2)
        mutant = delta * best_parent + (1 - delta) * current_parent + F * np.sum(half1 - half2)
        # krzyrzowanie
        child_positions.append(cross_function(current_parent, mutant))
    return child_positions

def best_k(population, objective_func, cross_function, k=1, F=0.5):
    number_of_candidates = k * 2
    swarm_current_fitness = np.array([objective_func(particle) for particle in population])
    best_index = np.argmin(swarm_current_fitness)
    parent = population[best_index]
    pop_size = len(population)
    child_positions = []
    for j in range(pop_size):
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates, replace=False)]
        half1, half2 = np.split(candidates, 2)
        mutant = parent + F * np.sum(half1 - half2)
        # krzyrzowanie
        child_positions.append(cross_function(parent, mutant))
    return child_positions

def rand_to_best_k(population, objective_func, cross_function, k=1, F=0.5, delta=0.5):
    number_of_candidates = k * 2
    swarm_current_fitness = np.array([objective_func(particle) for particle in population])
    best_index = np.argmin(swarm_current_fitness)
    parent = population[best_index]
    pop_size = len(population)
    child_positions = []
    for j in range(pop_size):
        possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
        candidates = population[np.random.choice(possible_candidates, number_of_candidates + 1, replace=False)]
        rand = candidates.delete(0)
        half1, half2 = np.split(candidates, 2)
        mutant = delta * parent + (1 - delta) * rand + F * np.sum(half1 - half2)
        # krzyrzowanie
        child_positions.append(cross_function(parent, mutant))
    return child_positions


def bin_cross_function(parent_a, parent_b, pc=0.5):
    dims = len(parent_a)
    p = np.random.rand(dims)

    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial


# todo to nie jest expo
def exp_cross_function(parent_a, parent_b, pc=0.5, D=2):
    dims = len(parent_a)
    p = np.random.rand(dims)
    d = 1
    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial
