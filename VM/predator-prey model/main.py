import numpy
import matplotlib.pyplot as plt
from predator import runge_kutta_method, Bogacki_Shampine_method, foo, boo
import math

def diffur1(x0, y0, a, b):
    return x0 * a - y0 * x0 * b


def diffur2(x0, y0, a, b):
    return -y0 * a + x0 * y0 * b


def default(data, alpha, delta):
    return -alpha * delta * data


if __name__ == '__main__':
    alpha = 5
    beta = 2
    gamma = 9
    delta = 3
    statX = gamma / delta
    statY = alpha / beta
    h = 0.01
    """eq = [100, 50]
    x = []
    y = []
    for i in range(4000):
        x.append(Bogacki_Shampine_method(eq, diffur1, alpha, beta, h) + eq[0])
        y.append(Bogacki_Shampine_method(eq, diffur2, gamma, delta, h) + eq[1])
        eq[0] = x[-1]
        eq[1] = y[-1]
   
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('Bogacki_Shampine_method')
    plt.savefig('Bogacki_Shampine_method')
    plt.show()"""

    t = numpy.linspace(0, 800, 800)
    eq = [statX + 0.8, statY + 0.5]
    x1 = []
    y1 = []
    for i in range(800):
        x1.append(runge_kutta_method(eq, diffur1, alpha, beta, h) + eq[0])
        y1.append(runge_kutta_method(eq, diffur2, gamma, delta, h) + eq[1])
        eq[0] = x1[-1]
        eq[1] = y1[-1]
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x1, "red", label="Жертвы")
    plt.plot(t, y1, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('runge_kutta_method1')
    plt.savefig('runge_kutta_method1')
    plt.show()

    t = numpy.linspace(0, 80, 800)
    eq = [statX + 0.8, statY + 0.5]
    x1 = []
    y1 = []
    for i in range(800):
        unsv = foo(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        x1.append(unsv[0])
        y1.append(unsv[1])
        eq[0] = x1[-1]
        eq[1] = y1[-1]
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x1, "red", label="Жертвы")
    plt.plot(t, y1, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('runge_kutta_method')
    plt.savefig('runge_kutta_method')
    plt.show()

    x = []
    y = []
    A =statX
    B = statY + 0.5
    t = numpy.linspace(0, 800, 800)
    omega = math.sqrt(alpha*gamma)
    for i in range(800):
        x.append(A*math.sin(i*omega))
        y.append(B*math.sin(omega*i))
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('осциллятор')
    plt.savefig('oscillator')
    plt.show()