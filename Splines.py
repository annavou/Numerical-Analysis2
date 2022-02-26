import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def Splines(x, y, xi):
    n = len(x)

    dx = np.zeros(n - 1)
    dy = np.zeros(n - 1)
    A = np.zeros((n, n))
    A[0, 0] = 1
    A[n - 1, n - 1] = 1
    B = np.zeros(n)

    for i in range(n - 1):
        dx[i] = x[i + 1] - x[i]
        dy[i] = y[i + 1] - y[i]

    for i in range(1, n - 1):
        A[i, i + 1] = dx[i]
        A[i, i - 1] = dx[i - 1]
        A[i, i] = 2 * (dx[i - 1] + dx[i])
        B[i] = 3 * (dy[i] / dx[i] - dy[i - 1] / dx[i - 1])

    b = np.zeros(n)
    d = np.zeros(n)
    c = np.linalg.solve(A, B)
    for i in range(n - 1):
        b[i] = dy[i] / dx[i] - dx[i] * (2 * c[i] + c[i + 1]) / 3
        d[i] = (c[i + 1] - c[i]) / (3 * dx[i])

    for i in range(n - 1):
        if x[i] <= xi <= x[i + 1]:
            S = y[i] + b[i] * (xi - x[i]) + c[i] * (xi - x[i]) ** 2 + d[i] * (xi - x[i]) ** 3

    return S


x = np.linspace(-np.pi, np.pi, 10)
y = f(x)
for i in x:
    s = Splines(x, y, i)
    print('%f' % s)

x2 = np.linspace(-np.pi, np.pi, 200)
y2 = f(x2)

og = np.zeros(200)
for i in range(200):
    og[i] = Splines(x, y, x2[i])

r = og - y2

SE = 0
for i in range(200):
    SE += pow(r[i], 2)
SE = np.sqrt(SE)
RMSE = SE / np.sqrt(200)
print('%f' % RMSE)

plt.title("Σφάλμα Μεθόδου Splines")
plt.ylabel("Σφάλμα")
plt.xlabel("x-label")
plt.plot(x2, r)
plt.ticklabel_format(style='plain')
plt.show()
