from matplotlib import pyplot as plt
import Zad3.fun.testFunctionParameters as testFunctionParameters

import Zad3.algo.pso as pso
import Zad3.algo.sma as sma


objective_func, dimensions, lower_bound, upper_bound, accuracy = testFunctionParameters.testFunctionParameters.SPHERE.value
print(testFunctionParameters.testFunctionParameters.HELP.value)

# dane inicializacyjne
pop_size = 200
max_iter = 1000

# parametry sma
w = 0.9
vb = 0.0

# parametry pso
# inercja(0,1) -> w
# komponent poznawczy(0,2) = przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze = c1
# komponent społeczny(0,2) = przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze = c2
# m - mutation probability
w_pso = 0.5
c1 = 1
c2 = 2
m = 0.5

best_pos, best_fit, history = pso.run_pso(objective_func, lower_bound, upper_bound, max_iter, pop_size, w_pso, c1, c2, m, 2)
print(best_fit)
print(history)
plt.title('Algorytm PSO')
plt.plot(history)
plt.yscale('log')
plt.show()

best_pos, best_fit, history = sma.run_alg(objective_func, lower_bound, upper_bound, max_iter, pop_size, w, vb, 2)
print(best_fit)
print(history)
plt.title('Algorytm SMA')
plt.plot(history)
plt.yscale('log')
plt.show()
