import numpy as np
from matplotlib import pyplot as plt

import Zad1.algo.pso as pso
import Zad1.algo.de as de
import Zad1.algo.tools as tools
from Zad1.algo.tools import swarm_generator
import Zad1.fun.testFunctionParameters as testFunctionParameters

nazwa, objective_func, dimensions, lower_bound, upper_bound, accuracy = testFunctionParameters.testFunctionParameters.ZAKHAROV.value
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

iter = 5
historie = []
for i in range(iter):
    swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
    wynik, historia = pso.pso(objective_func, swarm, w, c1, c2, max_iter, accuracy)
    historie.append(historia)

means = np.mean(historie, axis=0)
std_devs = np.std(historie, axis=0)
plt.errorbar(range(len(means)), means, yerr=std_devs, fmt='o', capsize=5)
plt.xticks(range(len(means)))
plt.title(nazwa+"-"+str(dimensions))
plt.xlabel('Oś X')
plt.ylabel('Oś Y')
plt.plot(historia)
plt.yscale('log')
plt.show()
