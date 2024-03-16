import numpy as np

# Przykładowa funkcja celu (minimum w punkcie (0,0))
def objective_func(x):
    return np.sum(np.square(x))

#inicjalizacja

#obszar przeszukiwań
lower_bound = -50
upper_bound = 50
dimensions = 2

#wielkosć populacji
pop_size = 10


#warunki stopu, max liczba pokolen, tolerancja
max_iter = 10
tol = 1e-6

# parametry
# inercja(0,1) -> w
# komponent poznawczy(0,2) = przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze = c1
# komponent społeczny(0,2) = przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze = c2
w = 0.2
c1 = 0.5
c2 = 0.5

#inicjalizacja pozycji początkowyc
#start_positions = [(particle, objective_func(particle)) for particle in population]
start_positions = np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimensions))
best_positions = start_positions
best_fitness_values = np.array([objective_func(individual) for individual in start_positions])

#najlepszy osonik
#todo aktualnie jest najniższy argument powinno być najbliższy? chociaż wszędzie f min =0 także chyba git
best_index = np.argmin(best_fitness_values)
best_solution = start_positions[best_index]
best_fitness = best_fitness_values[best_index]

#inicjalizacja inercji
inertia = np.zeros((pop_size, dimensions), dtype=int)
# PSO na 3
for i in range(max_iter):
    inertia = w * inertia
    cognitive_components = c1 * (best_positions - start_positions)
    social_components = c2 * (best_solution - start_positions)
    speed = inertia + cognitive_components + social_components
    new_positions = start_positions + speed
    new_fitness = np.array([objective_func(individual) for individual in new_positions])
    new_best_positions = []
    for j in range(pop_size):
        if best_fitness_values[j] > new_fitness[j]: new_best_positions.append(new_positions[j])
        else: new_best_positions.append(best_positions[j])
    best_positions = np.array(new_best_positions)
    if np.max(new_fitness) - np.min(new_fitness) < tol:
        break
    inertia = speed

print(best_positions)

