import numpy as np
import matplotlib.pyplot as plt
from fun.testFunctionParameters import testFunctionParameters as tfp
from zad2.boa import boa_na3

max_iter = 100
pop_size = 100
nr_of_runs = 1
#funkcje_test1 = [tfp.SPHERE, tfp.GRIEWANK, tfp.ROSENBROCK, tfp.BROWN,tfp.ACKLEY,tfp.F2]
funkcje_test1 = [tfp.SPHERE]
history = []
for fun in funkcje_test1:
    print("Function {}".format(fun))
    for i in range(nr_of_runs):
        print("Progres {}%".format(i*100/nr_of_runs))
        history.append(boa_na3(fun, pop_size, max_iter))
srednie = [sum(kolumna) / max_iter for kolumna in zip(*history)]
plt.bar(range(len(srednie)), srednie, color='skyblue')
plt.ylabel('Średnia wartość')
plt.title('Średnie wartości dla każdego indeksu kolumny')
plt.xticks(range(len(srednie)))
plt.grid(True)
plt.show()