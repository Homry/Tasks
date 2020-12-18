import numpy
import matplotlib.pyplot as plt
from predator import runge_kutta_method, Bogacki_Shampine_method, foo
import math


def diffur1(x0, y0, a, b):
    return x0 * a - y0 * x0 * b


def diffur2(x0, y0, a, b):
    return -y0 * a + x0 * y0 * b


def default(data, alpha, delta):
    return -alpha * delta * data


if __name__ == '__main__':
    alpha = 6
    beta = 4
    gamma = 8
    delta = 2
    statX = gamma / delta
    statY = alpha / beta
    t = numpy.linspace(0, 100000, 100000)
    h = 0.01
    ax = 0.8
    ay = 0.5
    eq = [statX + ax, statY + ay]
    x = []
    y = []
    for i in range(100000):
        unsv = Bogacki_Shampine_method(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        x.append(unsv[0])
        y.append(unsv[1])
        eq[0] = x[-1]
        eq[1] = y[-1]
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    amplx = xmin + (xmax - xmin)/2.0
    amply = ymin + (ymax - ymin)/2.0



    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    # plt.legend(loc='best')
    plt.title('Bogacki_Shampine_method')
    plt.show()


    print((xmax - xmin)/2.0, (ymax-ymin)/2.0)
    x2 = []
    y2 = []
    A = (xmax - xmin)/2.0
    B = (ymax - ymin)/2.0
    print(A, B)
    t = numpy.linspace(0, 100001, 100001)
    omega = math.sqrt(alpha * gamma)
    i = 0
    while i < 10:
        x2.append(A * math.sin(i * omega + math.pi *4145/5000.0))
        y2.append(B * math.sin(omega * i + math.pi * 1121/4000.0))
        i += 0.0001
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x2, "red", label="Жертвы")
    plt.plot(t, y2, "blue", label="Хищники")
    # plt.legend(loc='best')
    plt.title('осциллятор')
    #plt.show()
    print(x[0], y[0])
    print(x2[0], y2[0])



