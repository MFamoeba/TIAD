import math
from OptimizationTestFunctions import Fletcher
import numpy as np


def sphere_func(x):
    x = np.array(x)
    return np.sum(np.square(x))


def f2_function(x):
    x = np.array(x)
    n = len(x)
    sum1 = np.sum(100 * (x[1:] - x[:-1] ** 2) ** 2)
    sum2 = np.sum((x[:-1] - 1) ** 2)
    return sum1 + sum2


def rosenbrock_function(x):
    x = np.asarray_chkfinite(x)
    x0 = x[:-1]
    x1 = x[1:]
    return (sum((1 - x0) ** 2)
            + 100 * sum((x1 - x0 ** 2) ** 2))


def griewank_function(x):
    x = np.array(x)
    n = len(x)
    sum_sq = np.sum(x ** 2)
    prod_cos = np.prod(np.cos(x / np.sqrt(np.arange(1, n + 1))))
    return 1 + (sum_sq / 4000) - prod_cos


# git
def ackley_function(x):
    vec = np.array(x)
    s1 = sum((x * x for x in vec)) / vec.size
    s2 = sum((math.cos(2 * math.pi * x) for x in vec)) / vec.size

    return 20 + math.e - 20 * math.exp(-0.2 * s1) - math.exp(s2)



def brown_function(x):
    x = np.array(x)
    n = len(x)
    sum = 0
    for i in range(n - 1):
        sum += (x[i] ** 2) ** (x[i + 1] ** 2 + 1) + (x[i + 1] ** 2) ** (x[i] ** 2 + 1)
    return sum


def zakharov_function(x):
    x = np.array(x)
    n = len(x)
    sum1 = np.sum(pow(x, 2))
    sum2 = np.sum(np.arange(1, n + 1) * x)
    return sum1 + sum2 ** 2 + sum2 ** 4

def scheffer_function(vec):
    return 0.5 + sum(
        ((math.sin(vec[i] ** 2 - vec[i + 1] ** 2) ** 2 - 0.5) / (1 + 0.001 * (vec[i] ** 2 + vec[i + 1] ** 2)) ** 2 for i
         in range(vec.size - 1)))

def rastgrin_function(vec):
    s = sum((x * x - math.cos(math.pi*2 * x) * 10 for x in vec))

    return 10*len(vec) + s
