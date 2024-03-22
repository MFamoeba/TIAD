import numpy as np

lower_bound = -100
upper_bound = 100
dimensions = 20

# wielkosć populacji
pop_size = 200

# warunki stopu, max liczba pokolen, tolerancja
max_iter = 1000
tol = 1e-6

# parametry
# inercja(0,1) -> w
# komponent poznawczy(0,2) = przyspiesznie_poznawcze * ( najlepsza pozycja - aktualna) -> przyspieszenie_poznawcze = c1
# komponent społeczny(0,2) = przyspiesznie_społeczne * ( najlepsza pozycja w roju - aktualna) -> przyspieszenie poznawcze = c2
w = 0.5
c1 = 1
c2 = 2

swarm = swarm_generator(pop_size, lower_bound, upper_bound, dimensions)
wynik, historia = pso(objective_func, swarm, w, c1, c2, max_iter, tol)
print(historia)
plt.plot(historia)
plt.show()
