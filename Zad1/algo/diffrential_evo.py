import numpy as np


def devo(population, mutation_func, objective_func, cross_function, k=1, f=0.5, max_iter=100):
    population = np.array(population)
    for i in range(max_iter):
        mutation_func(population, objective_func, cross_function, k, f)
    return population


def curr_k(population, objective_func, cross_function, k=1, F=0.5):
    number_of_candidates = k * 2
    for j in range(pop_size):
        parent = population[j]
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


def exp_cross_function(parent_a, parent_b, pc=0.5, D=2):
    dims = len(parent_a)
    p = np.random.rand(dims)
    d = 1
    trial = [parent_b[i] if p[i] < pc else parent_a[i] for i in range(dims)]
    return trial

#Test functions
def sphere_func(x):
    return np.sum(np.square(x))


def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))


# obszar przeszukiwań
lower_bound = -50
upper_bound = 50
dimensions = 2

# wielkosć populacji
pop_size = 10
k = 1

swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
dupa = devo(swarm, curr_k, sphere_func, bin_cross_function, k)
print(dupa)
