import numpy as np
import matplotlib.pyplot as plt
from fun.testFunctionParameters import testFunctionParameters as tfp
from boa import boa_na3
from bat import bat

max_iter = 1000
pop_size = 150
nr_of_runs = 10
funkcje_test1 = [tfp.SPHERE, tfp.GRIEWANK, tfp.ROSENBROCK, tfp.BROWN,tfp.F2,tfp.RASTGRIN]
#funkcje_test1 = [tfp.SPHERE]
for fun in funkcje_test1:
    history = []
    history2 = []
    print("Function {}".format(fun))
    for i in range(nr_of_runs):
        print("Progres {}%".format(i*100/nr_of_runs))
        history.append(boa_na3(fun, pop_size, max_iter))
    srednie = [sum(kolumna) / nr_of_runs for kolumna in zip(*history)]
    name, objective_func, dim, lb, ub, accuracy = fun.value
    plt.plot(srednie)
    plt.title('Algorytm BAT: {}'.format(name))
    plt.yscale('log')
    plt.show()
    number = srednie.pop()
    print(f"{number:.4e}")

