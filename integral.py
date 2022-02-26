import numpy as np


def f(x):
    return np.sin(x)


def trapezoidal_meth(a, b, N):
    x = np.linspace(a, b, N + 1)
    M = np.abs(-np.sin(np.pi / 2))
    e = (pow(b - a, 3) / (12 * pow(N, 2))) * M
    s = 0
    for i in range(1, N):
        s += f(x[i])

    I = ((b - a) / (2 * N)) * (f(x[0]) + f(x[N]) + 2 * s)
    print(I)
    print('%f' % e)


def simpson_meth(a, b, N):
    x = np.linspace(a, b, N + 1)
    M = np.sin(np.pi / 2)
    e = (pow(b - a, 5) / (180 * pow(N, 4))) * M
    s1 = 0
    for i in range(1, N, 2):
        s1 += f(x[i])
    s2 = 0
    for i in range(2, N, 2):
        s2 += f(x[i])

    I = ((b - a) / (3 * N)) * (f(x[0]) + f(x[N]) + (2 * s2) + (4 * s1))
    print(I)
    print('%f' % e)


trapezoidal_meth(0, np.pi / 2, 11)
simpson_meth(0, np.pi / 2, 12)
