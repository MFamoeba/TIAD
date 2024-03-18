import numpy as np

def objective_func(x):
    return np.sum(np.square(x))
def pso(cost_func, swarm, w=0.5, c1=1, c2=2, max_iter=100, tol=1e-6):
    current_positions = np.array(swarm.copy())
    best_positions = current_positions.copy()

    swarm_best_fitness = np.array([cost_func(particle) for particle in current_positions])
    best_index = np.argmin(swarm_best_fitness)
    best_particle_position = current_positions[best_index]
    best_particle_fitness = swarm_best_fitness[best_index]

    pop_num = len(best_positions)
    dimensions_number = len(best_particle_position)
    inertia = np.zeros((pop_num, dimensions_number), dtype=float)

    for i in range(max_iter):
        linear_factor = 1  # (max_iter - i) / max_iter
        inertia = w * linear_factor * inertia
        r1 = np.random.uniform(0, 1, (pop_num, dimensions_number))
        r2 = np.random.uniform(0, 1, (pop_num, dimensions_number))
        cognitive_components = r1 * c1 * linear_factor * (best_positions - current_positions)
        social_components = r2 * c2 * linear_factor * (best_particle_position - current_positions)
        speed = inertia + cognitive_components + social_components

        inertia = inertia + speed
        current_positions = current_positions + speed

        swarm_current_fitness = np.array([cost_func(particle) for particle in current_positions])
        best_positions, swarm_best_fitness = find_new_best_positions(best_positions, current_positions, swarm_best_fitness, swarm_current_fitness)
        best_index = np.argmin(swarm_best_fitness)
        best_particle_position = current_positions[best_index]
        best_particle_fitness = swarm_best_fitness[best_index]

        if np.max(swarm_current_fitness) - np.min(swarm_current_fitness) < tol:
            break

    # Return the best solution found by the PSO algorithm
    return best_particle_position, best_particle_fitness


def find_new_best_positions(best_positions, current_positions, swarm_best_fitness, swarm_current_fitness):
    new_best_positions = []
    new_best_fitness = []
    for i in range(len(best_positions)):
        if swarm_best_fitness[i] < swarm_current_fitness[i]:
            new_best_positions.append(best_positions[i])
            new_best_fitness.append(swarm_best_fitness[i])
        else:
            new_best_positions.append(current_positions[i])
            new_best_fitness.append(swarm_current_fitness[i])
    return np.array(new_best_positions), np.array(new_best_fitness)


def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))


# obszar przeszukiwań
lower_bound = -100
upper_bound = 100
dimensions = 20

# wielkosć populacji
pop_size = 13

# warunki stopu, max liczba pokolen, tolerancja
max_iter = 100
tol = 1e-6

# parametry
# inercja(0,1) -> w
# komponent poznawczy(0,2) = przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze = c1
# komponent społeczny(0,2) = przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze = c2
w = 0.5
c1 = 1
c2 = 2

swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
wynik = pso(objective_func, swarm, w, c1, c2, max_iter, tol)
print(wynik)
