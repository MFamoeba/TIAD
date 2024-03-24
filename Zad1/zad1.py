import numpy as np
from matplotlib import pyplot as plt

import Zad1.algo.pso as pso
import Zad1.algo.de as de
import Zad1.algo.tools as tools
from Zad1.algo.tools import swarm_generator
import Zad1.fun.testFunctionParameters as testFunctionParameters

testFunct = testFunctionParameters.testFunctionParameters.GRIEWANK.value
nazwa, objective_func, dimensions, lower_bound, upper_bound, accuracy = testFunct
print(testFunctionParameters.testFunctionParameters.HELP.value)
print(objective_func, dimensions, lower_bound, upper_bound, accuracy)

# wielkosć populacji
pop_size = 300

# warunki stopu, max liczba pokolen, tolerancja
max_iter = 400

# parametry algorytmu pso
# k liczba wektorów różnicójących (max = pop - 1) zalezy od wykorzystanego algo w sumie
# f - współczynnik abplifikacji wektorów różnicujących (0,1)
# delta - współczynnik liniowa kombinacja osobnika (0,1) im większy tym bardziej najlepszy niż rodzic

f = 0.5
# parametry algorytmu pso
# inercja(0,1) ->
# w - współczynnik innercji
# komponent poznawczy = (0,2) * przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze =
# c1 - współczynnik poznawczy
# komponent społeczny = (0,2) * przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze =
# c2 - współczynnik społeczny
w = 0.5
c1 = 1
c2 = 2

swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
print("DE/curr_to_best/2/bin do " + nazwa + "\n" + "pc = 0.5, delta = 0.5, f = " + str(f))
# pierwsza
wynik, historia = de.devo(swarm, objective_func, de.curr_to_best_k, de.bin_cross_function, 2, f, max_iter, accuracy)

historia_best, historia_std = historia

fig, ax1 = plt.subplots()

fig.suptitle("DE/curr_to_best/2/bin do " + nazwa + "\n" + "pc = 0.5, delta = 0.5 f = " + str(f))
ax1.plot(historia_best, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel(nazwa + "(x)", color='b')
ax1.set_yscale('log')

# Create the second plot and share the x-axis with the first plot
ax2 = ax1.twinx()

# Plot the second function using red color
ax2.plot(historia_std, 'r-')
ax2.set_yscale('log')
ax2.set_ylabel('Odchylenie stadardowe', color='r')
plt.show()

# druga
print(
    "PSO DE/curr_to_best/2/bin do " + nazwa + "\npc = 0.5,  delta = 0.5" + ", f=" + str(f) + ", w = " + str(w) + ", c1 = " + str(
        c1) + ", c2 = " + str(c2))
wynik, historia = pso.pso_de(swarm, objective_func, de.curr_to_best_k, de.bin_cross_function, w, c1, c2, 2, f, max_iter,
                             accuracy)

historia_best, historia_std = historia

fig, ax1 = plt.subplots()

# Plot the first function using blue color
fig.suptitle(
    "PSO DE/curr_to_best/2/bin do " + nazwa + "\npc = 0.5,  delta = 0.5" + ", f=" + str(f) + ", w = " + str(w) + ", c1 = " + str(
        c1) + ", c2 = " + str(c2))
ax1.plot(historia_best, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel(nazwa + "(x)", color='b')
ax1.set_yscale('log')

# Create the second plot and share the x-axis with the first plot
ax2 = ax1.twinx()

# Plot the second function using red color
ax2.plot(historia_std, 'r-')
ax2.set_ylabel('Odchylenie stadardowe', color='r')
ax2.set_yscale('log')
plt.show()

# trzecia
print("PSO z DE/rand/5/bin do " + nazwa + "\n" + "pc = 0.5, f=" + str(f) + ", w = " + str(w) + ", c1 = " + str(
    c1) + ", c2 = " + str(c2))
wynik, historia = pso.pso_de(swarm, objective_func, de.rand_k, de.bin_cross_function, w, c1, c2, 5, f, max_iter,
                             accuracy)

historia_best, historia_std = historia

fig, ax1 = plt.subplots()

# Plot the first function using blue color
fig.suptitle("PSO z DE/rand/5/bin do " + nazwa + "\n" + "pc = 0.5, f=" + str(f) + ", w = " + str(w) + ", c1 = " + str(
    c1) + ", c2 = " + str(c2))
ax1.plot(historia_best, 'b-')
ax1.set_xlabel('X')
ax1.set_ylabel(nazwa + "(x)", color='b')
ax1.set_yscale('log')

# Create the second plot and share the x-axis with the first plot
ax2 = ax1.twinx()

# Plot the second function using red color
ax2.plot(historia_std, 'r-')
ax2.set_yscale('log')
ax2.set_ylabel('Odchylenie stadardowe', color='r')
plt.show()
