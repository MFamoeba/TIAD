import numpy as np

def objective_func(x):
    return np.sum(np.square(x))

def boundary(x, lb, ub):
    if x < lb:
        x = lb
    if x > ub:
        x = ub

    return x

def swarm_generator(pop_size=30, lower_bound=-5, upper_bound=5, dimension=20):
    return np.random.uniform(low=lower_bound, high=upper_bound, size=(pop_size, dimension))


pop_size = 30
lower_bound = -5
upper_bound = 5

dimension = 20
"""poszukując pożywienia emitują sygnał audio o zmiennej
częstotliwości w zakresie [fmin ,fmax], zmiennej długości fali
echolokacyjnej l
i o głośności Ai """
fmin = 0
fmax = 100
l = 2
"""wartość głośności jest zmienna - od dużej wartości dodatniej A0
do minimalnej wartości stałej Amin"""
Amax = 2
Amin = 1
"""w zależności od odległości od celu automatycznie dostosowują
długość fali (lub częstotliwość) emitowanych przez siebie
impulsów/sygnałów oraz szybkość emisji impulsów r  [0, 1]
"""
r = 1
Rmin = 0
Rmax = 1
# losowa inicjalizacja parametrów dla każdego nietoperza:pozycji x0 oraz prędkości v0
bat_postions = np.random.uniform(lower_bound, upper_bound, (pop_size, dimension))
bat_speeds = np.zeros_like(bat_postions)
"""wyznacznie częstowtliwości fi = fmin + (fmax - fmin) * beta
gdzie beta jest wektorem losowym o równomiernym rozkładzie z przedziału [0,1]
wyznaczenie aktualnego przystosowania 
"""
bat_fitness = np.zeros(pop_size)
bat_A = np.random.uniform(Amin, Amax, pop_size)
bat_r = np.random.uniform(Rmin, Rmax, pop_size)
for i in range(pop_size):
    bat_fitness[i] = objective_func(bat_postions[i])
"""ustalenie nietoperza o najlepszym przystosowaniu x
best - aktualnie najlepsze położenie"""
best_index = np.argmin(bat_fitness)
"""zainicjowanie wartości częstości tętna (ri
) i głośności (Ai
). Początkowa głośność A0 [1, 2]"""
A = 2
# współczynnik alfa od 0 do 1 stała zmiany głośności
alfa = 0.8
#, a początkowa szybkość emisji r0 [0, 1].
r = 1
# współczynnik gamma od 0 stała zmiany częstości
gamma = 0.8
"""INICJALIZACJA DONE"""
"""Przebieg"""
t_max = 100
for j in range(t_max):
    # krok drugi aktualizacja pozycji
    if j == 99:
        print("dupa")
    beta = np.random.uniform(0, 1, pop_size)
    bat_frequencies = fmin + (fmax - fmin) * beta
    A_avg = np.mean(bat_A)
    for i in range(pop_size):
        bat_speeds[i] = bat_speeds[i] + (bat_postions[i] - bat_postions[best_index]) * bat_frequencies[i]
        bat_postions[i] = bat_postions[i] + bat_speeds[i]
        if np.random.rand() > bat_r[i]:
            #e = rand <-1, 1>
            epsilon = np.random.rand()*2-1
            bat_postions[i] = bat_postions[i]+epsilon*A_avg
        boundary(bat_postions, lower_bound, upper_bound)
        #krok4
        if (np.random.rand() > bat_r[i]) and (objective_func(bat_postions[i])<bat_fitness[best_index]):
            bat_A[i] = alfa * bat_A[i]
            bat_r[i] = bat_r[i]*(1-np.exp(-gamma*j))
        #krok5
    for i in range(pop_size):
        bat_fitness[i] = objective_func(bat_postions[i])
    best_index = np.argmin(bat_fitness)
    print("Iter"+str(j))
    print("Best= "+str(bat_postions[best_index]))


    """nowe położenie jest generowane losowo i akceptowane z pewną bliskością
    w zależności od parametru Ai
    . W miarę zbliżania się nietoperza do ofiary
    głośność spada, a liczba emitowanych impulsów nietoperza wzrasta.
    Równanie aktualizacji głośności i częstości impulsów:
    """
    A=alfa*A
    r = r*(1-np.exp(-gamma*j))
    bat_fitness = np.array([objective_func(bat) for bat in bat_postions])
