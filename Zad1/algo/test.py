import numpy as np


def objective_func(x):
    return np.sum(np.square(x))

def differential_evo(population,objective_func, F = 0.5):
    population = np.array(population)
    for i in range(max_iter):
        # iter po wszystkich osobnikach
        for j in range(pop_size):
            parent = population[j]
            candidates = [candidate for candidate in range(pop_size) if candidate != j]
            a, b, c = swarm[np.random.choice(candidates, 3, replace=False)]
            mutant = a + F * (b - c)
            # krzyrzowanie
            child = bin_cross_function(parent, mutant)
            swarm[j] = child if objective_func(child) < objective_func(parent) else parent

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
lower_bound = -5
upper_bound = 5
dimensions = 2

# wielkosć populacji
pop_size = 10

# warunki stopu, max liczba pokolen, tolerancja
max_iter = 100

# współczynnik amplifikacji
F = 0.5
# współczynnik krzyżowania jest prawdopodobieństwem przejścia elementu z wektora mutanta vi do wektora
# próbnego
CR = 0.5
swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)



