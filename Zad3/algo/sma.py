import math
import random
DIM_NUMBER = 20


def run_alg(function: (), lower_bound: float, upper_bound: float, iterations: int, pop_size: int, w: float, vb: float):
    positions = [
        [random.uniform(lower_bound, upper_bound) for _ in range(DIM_NUMBER)] for _ in range(pop_size)
    ]

    best_particle_history = []

    for i in range(iterations):
        fitness = [function(position) for position in positions]
        positions = [position for _, position in sorted(zip(fitness, positions))]

        best_particle_history.append(function(positions[0]))

        w = w * math.exp(-i / iterations)

        # update positions

        for j in range(pop_size):
            if random.uniform(0, 1) < w:
                # approach food
                best_position = positions[0]
                r = random.uniform(0, 1)
                for k in range(DIM_NUMBER):
                    positions[j][k] = positions[j][k] + r * (best_position[k] - positions[j][k])
            else:
                # move randomly
                random_position = positions[random.randint(0, pop_size - 1)]
                r = random.uniform(0, 1)
                for k in range(DIM_NUMBER):
                    positions[j][k] = positions[j][k] + r * (random_position[k] - positions[j][k])
            # vibrate
            for k in range(DIM_NUMBER):
                positions[j][k] = positions[j][k] + random.uniform(-vb, vb)

            # check boundaries
            for k in range(DIM_NUMBER):
                if positions[j][k] < lower_bound:
                    positions[j][k] = lower_bound
                elif positions[j][k] > upper_bound:
                    positions[j][k] = upper_bound

    return positions[0], function(positions[0]), best_particle_history
