from enum import Enum
import Zad1.fun.test_functions as ts


class testFunctionParameters(Enum):
    HELP = ("Name","test_function", "dimensions", "lower_bound", "upper_bound", "accuracy")
    SPHERE = ("Funkcja sfery",ts.sphere_func, 20, -100, 100, 1e-4)
    F2 = ("Funkcja F2",ts.f2_function, 20, -100, 100, 1e-4)
    ROSENBROCK = ("Funkcja Rosenbrocka",ts.rosenbrock_function, 20, -2048, 2048, 30)
    GRIEWANK = ("Funkcja Griewanka",ts.griewank_function, 20, -600, 600, 0.1)
    ACKLEY = ("Funkcja Ackleya",ts.ackley_function, 20, -32, 32, 1e-4)
    BROWN = ("Funkcja Browna",ts.brown_function, 20, -1, 4, 1e-3)
    ZAKHAROV = ("Funkcja Zakharowa",ts.zakharov_function, 20, -10, 10, 1e-3)
