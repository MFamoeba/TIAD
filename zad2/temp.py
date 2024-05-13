print("Function {}".format(fun))
for i in range(nr_of_runs):
    print("Progres {}%".format(i * 100 / nr_of_runs))
    history2.append(boa_na3(fun, pop_size, max_iter))
srednie2 = [sum(kolumna) / nr_of_runs for kolumna in zip(*history2)]
name, objective_func, dim, lb, ub, accuracy = fun.value
plt.plot(srednie2)
plt.title('Algorytm BOA: {}'.format(name))
plt.yscale('log')
plt.show()
number = srednie2.pop()
print(f"{number:.4e}")