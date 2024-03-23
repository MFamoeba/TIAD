import numpy as np
from matplotlib import pyplot as plt

import Zad1.algo.pso as pso
import Zad1.algo.de as de
import Zad1.algo.tools as tools
from Zad1.algo.tools import swarm_generator
import Zad1.fun.testFunctionParameters as testFunctionParameters

objective_func, dimensions, lower_bound, upper_bound, accuracy = testFunctionParameters.testFunctionParameters.SPHERE.value
print(testFunctionParameters.testFunctionParameters.HELP.value)
print(objective_func, dimensions, lower_bound, upper_bound, accuracy)

# wielkosć populacji
pop_size = 200

# warunki stopu, max liczba pokolen, tolerancja
max_iter = 1000

# parametry
# inercja(0,1) -> w
# komponent poznawczy(0,2) = przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze = c1
# komponent społeczny(0,2) = przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze = c2
w = 0.5
c1 = 1
c2 = 2

swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
#wynik, historia = pso.pso(tools.griewank_function, swarm, w, c1, c2, max_iter, tol)
#print(historia)
#plt.plot(historia)
#plt.yscale('log')
#plt.show()
