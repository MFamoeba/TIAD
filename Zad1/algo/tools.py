import numpy as np

def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))

