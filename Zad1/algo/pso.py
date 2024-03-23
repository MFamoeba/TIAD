import numpy as np
import Zad1.algo.de as dv
from Zad1.algo.tools import find_new_best_positions


def pso_de(objective_func, swarm, k=1, f=0.5, w=0.5, c1=1, c2=2, tol=1e-6, max_iter=500):
    current_positions = np.array(swarm.copy())
    best_positions = current_positions.copy()

    swarm_best_fitness = np.array([objective_func(particle) for particle in current_positions])
    best_index = np.argmin(swarm_best_fitness)
    best_particle_position = current_positions[best_index]
    best_particle_fitness = swarm_best_fitness[best_index]

    pop_num = len(best_positions)
    dimensions_number = len(best_particle_position)
    inertia = np.zeros((pop_num, dimensions_number), dtype=float)
    best_particle_history = [best_particle_fitness]
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

        best_positions, swarm_best_fitness, current_positions_fitness = find_new_best_positions(best_positions,
                                                                                                current_positions,
                                                                                                objective_func)

        dv.curr_k(best_positions, objective_func, dv.bin_cross_function, k, f)
        best_index = np.argmin(swarm_best_fitness)
        best_particle_position = current_positions[best_index]
        best_particle_fitness = swarm_best_fitness[best_index]
        best_particle_history.append(best_particle_fitness)
        # stop after achiving certain accuracy
        #   if np.max(swarm_current_fitness) - np.min(swarm_current_fitness) < tol:
        #       break

    # Return the best solution found by the PSO algorithm
    return best_particle_position, best_particle_history


def pso(objective_func, swarm, w=0.5, c1=1, c2=2, max_iter=100, tol=1e-6):
    current_positions = np.array(swarm.copy())
    best_positions = current_positions.copy()

    swarm_best_fitness = np.array([objective_func(particle) for particle in current_positions])
    best_index = np.argmin(swarm_best_fitness)
    best_particle_position = current_positions[best_index]
    best_particle_fitness = swarm_best_fitness[best_index]

    pop_num = len(best_positions)
    dimensions_number = len(best_particle_position)
    inertia = np.zeros((pop_num, dimensions_number), dtype=float)
    best_particle_history = [best_particle_fitness]
    for i in range(max_iter):
        linear_factor = 1  # opcja na 3 (max_iter - i) / max_iter
        inertia = w * linear_factor * inertia
        r1 = np.random.uniform(0, 1, (pop_num, dimensions_number))
        r2 = np.random.uniform(0, 1, (pop_num, dimensions_number))
        cognitive_components = r1 * c1 * linear_factor * (best_positions - current_positions)
        social_components = r2 * c2 * linear_factor * (best_particle_position - current_positions)
        speed = inertia + cognitive_components + social_components

        inertia = inertia + speed
        current_positions = current_positions + speed
        best_positions, swarm_best_fitness, swarm_current_fitness = find_new_best_positions(best_positions, current_positions,
                                                                     objective_func)
        best_index = np.argmin(swarm_best_fitness)
        best_particle_position = current_positions[best_index]
        best_particle_fitness = swarm_best_fitness[best_index]
        best_particle_history.append(best_particle_fitness)
        # stop after achiving certain accuracy
        #   if np.max(swarm_current_fitness) - np.min(swarm_current_fitness) < tol:
        #       break

    # Return the best solution found by the PSO algorithm
    return best_particle_position, best_particle_history
