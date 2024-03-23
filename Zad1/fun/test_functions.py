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
    x = np.array(x)
    n = len(x)
    sum = 0
    for i in range(n - 1):
        sum += 100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2
    return sum


def griewank_function(x):
    x = np.array(x)
    n = len(x)
    sum_sq = np.sum(x ** 2)
    prod_cos = np.prod(np.cos(x / np.sqrt(np.arange(1, n + 1))))
    return 1 + (sum_sq / 4000) - prod_cos


# git
def ackley_function(x):
    x = np.array(x)
    n = len(x)
    sum1 = np.sum(x ** 2)
    sum2 = np.sum(np.cos(2 * np.pi * x))
    return -20 * np.exp(-0.2 * np.sqrt(sum1 / n)) - np.exp(sum2 / n) + 20 + np.exp(1)


# todo
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
