import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def lagrange(x, y, xi):
    n = len(x)
    p = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xi - x[j]) / (x[i] - x[j])

        p += L * y[i]

    return p


x = np.linspace(-np.pi, np.pi, 10)
y = f(x)
for i in x:
    p = lagrange(x, y, i)
    print('%f' % p)

x2 = np.linspace(-np.pi, np.pi, 200)
y2 = f(x2)
og = np.zeros(200)
for i in range(200):
    og[i] = lagrange(x, y, x2[i])

r = og - y2
SE = 0
for i in range(200):
    SE += pow(r[i], 2)
SE = np.sqrt(SE)
RMSE = SE / np.sqrt(200)
print('%f' % RMSE)

plt.title("Σφάλμα Πολυωνύμου Lagrange")
plt.ylabel("Σφάλμα")
plt.xlabel("x-label")
plt.plot(x2, r)
plt.ticklabel_format(style='plain')
plt.show()
