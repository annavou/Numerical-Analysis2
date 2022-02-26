import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)


def least_squares(x, y, xi, degree):
    b = y.copy()
    A = np.zeros((len(x), degree+1))

    for i in range(len(x)):
        for j in range(degree+1):
            A[i, j] = x[i] ** j

    at = A.T
    p1 = np.dot(at, A)
    p2 = np.dot(at, b)
    p = np.linalg.solve(p1, p2)

    s = 0
    for i in range(degree+1):
        s += p[i] * xi ** i

    return s


x = np.linspace(-np.pi, np.pi, 10)
y = f(x)
for i in x:
    s = least_squares(x, y, i, 6)
    print('%f' % s)

x2 = np.linspace(-np.pi, np.pi, 200)
y2 = f(x2)

og = np.zeros(200)
for i in range(200):
    og[i] = least_squares(x, y, x2[i], 6)

r = og - y2

SE = 0
for i in range(200):
    SE += pow(r[i], 2)
SE = np.sqrt(SE)
RMSE = SE / np.sqrt(200)
print('%f' % RMSE)

plt.title("Σφάλμα Ελαχίστων Τετραγώνων")
plt.ylabel("Σφάλμα")
plt.xlabel("x-label")
plt.plot(x2, r)
plt.ticklabel_format(style='plain')
plt.show()
