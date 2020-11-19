import numpy
import matplotlib.pyplot as plt
from methods import runge_kutta_method, Bogacki_Shampine_method


def diffur1(x0, y0, a, b):
    return x0 * a - y0 * x0 * b


def diffur2(x0, y0, a, b):
    return -y0 * a + x0 * y0 * b


if __name__ == '__main__':
    alpha = 1
    beta = 1
    gamma = 1
    delta = 1
    h = 0.01
    eq = [3, 1]
    x = []
    y = []
    for i in range(4000):
        x.append(Bogacki_Shampine_method(eq, diffur1, alpha, beta, h) + eq[0])
        y.append(Bogacki_Shampine_method(eq, diffur2, gamma, delta, h) + eq[1])
        eq[0] = x[-1]
        eq[1] = y[-1]
    t = numpy.linspace(0, 1000, 4000)
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc = 'best')
    plt.title('Bogacki_Shampine_method')
    plt.savefig('Bogacki_Shampine_method')
    plt.show()

    eq = [3, 1]
    x = []
    y = []
    for i in range(4000):
        x.append(runge_kutta_method(eq, diffur1, alpha, beta, h) + eq[0])
        y.append(runge_kutta_method(eq, diffur2, gamma, delta, h) + eq[1])
        eq[0] = x[-1]
        eq[1] = y[-1]
    t = numpy.linspace(0, 1000, 4000)
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc = 'best')
    plt.title('runge_kutta_method')
    plt.savefig('runge_kutta_method')
    plt.show()
