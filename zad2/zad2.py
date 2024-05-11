import numpy as np


def objective_func(x):
    return np.sum(np.square(x))


def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=2):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))


pop_size = 30
lower_bound = -5
upper_bound = 5
dimension = 2
"""poszukując pożywienia emitują sygnał audio o zmiennej
częstotliwości w zakresie [fmin ,fmax], zmiennej długości fali
echolokacyjnej l
i o głośności Ai """
fmin = 0
fmax = 1
l = 2
"""wartość głośności jest zmienna - od dużej wartości dodatniej A0
do minimalnej wartości stałej Amin"""
Amax = 30
Amin = 0.03
"""w zależności od odległości od celu automatycznie dostosowują
długość fali (lub częstotliwość) emitowanych przez siebie
impulsów/sygnałów oraz szybkość emisji impulsów r  [0, 1]
"""
r = 1
# losowa inicjalizacja parametrów dla każdego nietoperza:pozycji x0 oraz prędkości v0
bat_postions = np.random.uniform(lower_bound, upper_bound, (pop_size, dimension))
bat_speeds = np.random.uniform(lower_bound, upper_bound, (pop_size, dimension))
"""wyznacznie częstowtliwości fi = fmin + (fmax - fmin) * beta
gdzie beta jest wektorem losowym o równomiernym rozkładzie z przedziału [0,1]
wyznaczenie aktualnego przystosowania 
"""
bat_fitness = np.zeros(pop_size)
bat_frequencies = np.zeros(pop_size)
for i in range(pop_size):
    beta = np.random.uniform(0, 1, (pop_size, dimension))
    bat_frequencies[i] = fmin + (fmax - fmin) * beta
    bat_fitness[i] = objective_func(bat_postions[i])
"""ustalenie nietoperza o najlepszym przystosowaniu x
best - aktualnie najlepsze położenie"""
best_index = np.argmin(bat_fitness)
"""zainicjowanie wartości częstości tętna (ri
) i głośności (Ai
). Początkowa głośność A0 [1, 2], a początkowa szybkość emisji r0 [0, 1]."""
A = 2
r = 1
"""INICJALIZACJA DONE"""
"""Przebieg"""

#krok drugi aktualizacja pozycji
for i in range(pop_size):
    bat_speeds[i] = bat_speeds[i] + (bat_postions[i]-bat_postions[best_index])*bat_frequencies[i]
    bat_postions[i] = bat_postions[i] + bat_speeds[i]
"""nowe położenie jest generowane losowo i akceptowane z pewną bliskością
w zależności od parametru Ai
. W miarę zbliżania się nietoperza do ofiary
głośność spada, a liczba emitowanych impulsów nietoperza wzrasta.
Równanie aktualizacji głośności i częstości impulsów:
"""

#alfa od 0 do 1 stała
alfa = 0.8
bat_amplitude = np.full(pop_size, Azero)
bat_rate = np.zeros(pop_size)
for i in range(pop_size):
    bat_amplitude[i] = alfa*bat_amplitude[i]
