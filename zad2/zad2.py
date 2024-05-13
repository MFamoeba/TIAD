import numpy as np
import matplotlib.pyplot as plt
from fun.testFunctionParameters import testFunctionParameters as tfp
from boa import boa_na3
from bat import bat

max_iter = 1000
pop_size = 150
nr_of_runs = 1
#funkcje_test1 = [tfp.SPHERE, tfp.GRIEWANK, tfp.ROSENBROCK, tfp.BROWN,tfp.ACKLEY,tfp.F2,tfp.SCHEFFER,tfp.RASTGRIN]
funkcje_test1 = [tfp.RASTGRIN]
history = []
for fun in funkcje_test1:
    print("Function {}".format(fun))
    for i in range(nr_of_runs):
        print("Progres {}%".format(i*100/nr_of_runs))
        history.append(bat(fun, pop_size, max_iter))
    srednie = [sum(kolumna) / max_iter for kolumna in zip(*history)]
    plt.plot(srednie)
    plt.title('Średnia wartość wartośći funkcji celu: {}'.format(fun))
    plt.yscale('log')
    plt.show()
