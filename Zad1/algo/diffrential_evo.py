import numpy as np


def objective_func(x):
    return np.sum(np.square(x))

def devo(population,objective_func, F = 0.5, max_iter = 100):
    population = np.array(population)
    pop_size = len(population)
    for i in range(max_iter):
        # iter po wszystkich osobnikach
        for j in range(pop_size):
            parent = population[j]
            candidates = [candidate for candidate in range(pop_size) if candidate != j]
            a, b, c = population[np.random.choice(candidates, 3, replace=False)]
            mutant = a + F * (b - c)
            # krzyrzowanie
            child = bin_cross_function(parent, mutant)
            population[j] = child if objective_func(child) < objective_func(parent) else parent
    return population
def devo_rand_1_bin(population,objective_func, F = 0.5, max_iter = 100):
    population = np.array(population)
    pop_size = len(population)
    for i in range(max_iter):
        for j in range(pop_size):
            parent = population[j]
            candidates = [candidate for candidate in range(pop_size) if candidate != j]
            a, b, c = population[np.random.choice(candidates, 3, replace=False)]
            mutant = a + F * (b - c)
            # krzyrzowanie
            child = bin_cross_function(parent, mutant)
            population[j] = child if objective_func(child) < objective_func(parent) else parent
    return population

def devo_rand_k_bin(population,objective_func,k=5, F = 0.5, max_iter = 100):
    population = np.array(population)
    pop_size = len(population)
    for i in range(max_iter):
        for j in range(pop_size):
            parent = population[j]
            possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
            candidates = population[np.random.choice(possible_candidates, k+1, replace=False)]
            x1 = np.delete(candidates, 0)
            half1, half2 = np.split(candidates, 2)
            mutant = x1 + F * np.sum(half1-half2)
            # krzyrzowanie
            child = bin_cross_function(parent, mutant)
            population[j] = child if objective_func(child) < objective_func(parent) else parent
    return population

def devo_current_k_bin(population,objective_func,k=5, F = 0.5, max_iter = 100):
    population = np.array(population)
    pop_size = len(population)
    for i in range(max_iter):
        for j in range(pop_size):
            parent = population[j]
            possible_candidates = [candidate for candidate in range(pop_size) if candidate != j]
            candidates = population[np.random.choice(possible_candidates, k+1, replace=False)]
            x1 = np.delete(candidates, 0)
            half1, half2 = np.split(candidates, 2)
            mutant = x1 + F * np.sum(half1-half2)
            # krzyrzowanie
            child = bin_cross_function(parent, mutant)
            population[j] = child if objective_func(child) < objective_func(parent) else parent
    return population
def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))

def bin_cross_function(parent_a, parent_b, pc=0.5):
    dims = len(parent_a)
    p = np.random.rand(dims)

    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial


def exp_cross_function(parent_a, parent_b, pc=0.5, D = 2):
    dims = len(parent_a)
    p = np.random.rand(dims)
    d = 1
    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial

# obszar przeszukiwań
lower_bound = -50
upper_bound = 50
dimensions = 2

# wielkosć populacji
pop_size = 10
swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
dupa = devo_rand_k_bin(swarm, objective_func)
print(dupa)