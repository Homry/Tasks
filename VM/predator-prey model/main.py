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
   
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('Bogacki_Shampine_method')
    plt.savefig('Bogacki_Shampine_method')
    plt.show()

    eq = [statX + 0.8, statY + 0.5]
    x1 = []
    y1 = []
    h = 0.0001
    t = numpy.linspace(0, 100000, 100000)
    for i in range(100000):
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
    plt.savefig('runge_kutta_method1')
    plt.show()

    errorx = []
    errory =[]
    for i in range(100000):
        errorx.append(x[i]-x1[i])
        errory.append(y[i]-y1[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('разница_методов')
    plt.savefig('разница_методов')
    plt.show()

    x1min = min(x1)
    x1max = max(x1)
    y1min = min(y1)
    y1max = max(y1)
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    amplx = xmin + (xmax - xmin) / 2.0
    amply = ymin + (ymax - ymin) / 2.0
    amplx1 = x1min + (x1max - x1min) / 2.0
    amply1 = y1min + (y1max - y1min) / 2.0

    x2 = []
    y2 = []
    A = ((xmax - xmin) / 2.0 + (x1max - x1min) / 2.0) / 2.0
    B = ((ymax - ymin) / 2.0 + (y1max - y1min) / 2.0) / 2.0
    t = numpy.linspace(0, 100001, 100001)
    omega = math.sqrt(alpha*gamma)
    i = 0
    while i < 10:
        x2.append(A * math.sin(i * omega + math.pi * 4145 / 5000.0))
        y2.append(B * math.sin(omega * i + math.pi * 1121 / 4000.0))
        i += 0.0001
    print(len(x2))
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x2, "red", label="Жертвы")
    plt.plot(t, y2, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('осциллятор')
    plt.savefig('oscillator')
    plt.show()



    print(x1min, x1max, y1min, y1max)
    print(xmin, xmax, ymin, ymax)
    print(x[0], x1[0], x2[0], '- x0')
    print(y[0], y1[0], y2[0], '-y0')


    errorx = []
    errory = []
    t = numpy.linspace(0, 100000, 100000)
    for i in range(len(x)):
        errorx.append((x[i] - xmin - (xmax - xmin)/2) - x2[i])
        errory.append((y[i] - ymin - (ymax - ymin)/2) - y2[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('ошибка1')
    plt.savefig('ошибка1')
    plt.show()
    t = numpy.linspace(0, 100000, 100000)
    print(len(x1))
    print(len(x2))
    errorx.clear()
    errory.clear()

    for i in range(len(x)):
        errorx.append(x1[i] - amplx1 - x2[i])
        errory.append(y1[i] - amply1 - y2[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('ошибка2')
    plt.savefig('ошибка2')
    plt.show()
    print(x[0], y[0])
    print(x1[0], y1[0])
    print('амплитуда x', (xmax - xmin) )
    print('амплитуда y', (ymax - ymin) )