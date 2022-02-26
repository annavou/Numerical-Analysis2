import numpy as np


def least_squares(x, y, xi, degree):
    b = y.copy()
    A = np.zeros((len(x), degree + 1))

    for i in range(len(x)):
        for j in range(degree + 1):
            A[i, j] = x[i] ** j

    at = A.T
    p1 = np.dot(at, A)
    p2 = np.dot(at, b)
    p = np.linalg.solve(p1, p2)

    s = 0
    for i in range(degree + 1):
        s += p[i] * xi ** i

    return s


# OTE
x = [29, 30, 1, 2, 3, 6, 7, 8, 9, 10]
y = [15.1500, 15.2550, 15.4100, 15.4700, 15.3900, 15.5000, 15.5700, 15.7800, 16.1000, 16.0800]
y2 = [16.2500, 16.3200, 16.3800, 16.2550, 15.9500]
res = np.zeros(5)
xi = [14, 15, 16, 17, 20]
for i in range(5):
    res[i] = least_squares(x, y, xi[i], 4)
print(res)
r1 = res - y2

SE = 0
for i in range(5):
    SE += pow(r1[i], 2)
SE = np.sqrt(SE)
RMSE = SE / np.sqrt(5)
print('%f' % RMSE)

# ETE
x1 = [29, 30, 1, 2, 3, 6, 7, 8, 9, 10]
y1 = [2.6300, 2.6370, 2.6950, 2.6900, 2.7630, 2.7260, 2.800, 2.8500, 2.8280, 2.8490]
y3 = [2.8250, 2.8300, 2.9090, 2.8500, 2.7880]
res2 = np.zeros(5)
xi = [14, 15, 16, 17, 20]
for i in range(5):
    res2[i] = least_squares(x1, y1, xi[i], 4)
print(res2)
r2 = res2 - y3

SE = 0
for i in range(5):
    SE += pow(r2[i], 2)
SE = np.sqrt(SE)
RMSE = SE / np.sqrt(5)
print('%f' % RMSE)
