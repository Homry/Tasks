import numpy
import matplotlib.pyplot as plt
from predator import *
import math
import time


def diffur1(x0, y0, a, b):
    return x0 * a - y0 * x0 * b


def diffur2(x0, y0, a, b):
    return -y0 * a + x0 * y0 * b


def default(data, alpha, delta):
    return -alpha * delta * data


if __name__ == '__main__':
    alpha = 6.0
    beta = 4.0
    gamma = 8.0
    delta = 2.0
    statX = gamma / delta
    statY = alpha / beta
    n = 1000
    h = 1e-12
    ax = 1.0
    ay = 0.5
    eq = [statX + ax, statY + ay]
    x = []
    y = []
    t = []
    start_time = time.time()
    for i in range(n):
        unsv = Bogacki_Shampine_method(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        x.append(unsv[0])
        y.append(unsv[1])

        eq[0] = x[-1]
        eq[1] = y[-1]

        t.append(h * i)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, x, "red", label="Жертвы")
    plt.plot(t, y, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('Bogacki_Shampine_method')
    plt.savefig('Bogacki_Shampine_method')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))
    T = 1e-4
    h= 0.1
    eq = [statX + ax, statY + ay]
    xt = []
    yt = []
    tt = []
    start_time = time.time()
    for i in range(n):
        unsv = Bogacki_Shampine_method(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        xt.append(unsv[0])
        yt.append(unsv[1])
        unsv = Bogacki_Shampine_method(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        epsX = ((xt[-1]-unsv[0])/((math.pow(2, 4)) - 1))
        epsY = ((yt[-1] - unsv[1]) / ((math.pow(2, 4)) - 1))
        if(epsX > T or epsY > T):
            eps = max(epsX-T, epsY-T)
            h = 0.1*h*math.pow((T/eps),(1/4))
        print(h)
        #print(epsX, epsY)
        eq[0] = xt[-1]
        eq[1] = yt[-1]

        tt.append(h * i)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(tt, xt, "red", label="Жертвы")
    plt.plot(tt, yt, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('Bogacki_Shampine_method_auto')
    plt.savefig('Bogacki_Shampine_method_auto')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))
    n = 1000
    eq = [statX + ax, statY + ay]
    x1 = []
    y1 = []
    h = 1e-14
    t1 = []
    start_time = time.time()
    for i in range(n):
        unsv = foo(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        x1.append(unsv[0])
        y1.append(unsv[1])
        eq[0] = x1[-1]
        eq[1] = y1[-1]
        t1.append(h * i)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t1, x1, "red", label="Жертвы")
    plt.plot(t1, y1, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('runge_kutta_method')
    plt.savefig('runge_kutta_method1')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))

    eq = [statX + ax, statY + ay]
    x3 = []
    y3 = []
    h = 1e-13
    t3 = []
    start_time = time.time()
    for i in range(n):
        unsv = Adams(eq, diffur1, diffur2, alpha, beta, gamma, delta, h)
        x3.append(unsv[0])
        y3.append(unsv[1])
        eq[0] = x3[-1]
        eq[1] = y3[-1]
        t3.append(h * i)
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t3, x3, "red", label="Жертвы")
    plt.plot(t3, y3, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('adams_method')
    plt.savefig('adams_method1')
    plt.show()
    print("--- %s seconds ---" % (time.time() - start_time))

    errorx = []
    errory = []
    x3int = list(numpy.interp(t, t3, x3))
    y3int = list(numpy.interp(t, t3, y3))
    for i in range(n):
        errorx.append(x3int[i] - x[i])
        errory.append(y3int[i] - y[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('разница_методов3')
    plt.savefig('разница_методов3')
    plt.show()

    errorx = []
    errory = []
    x3int = list(numpy.interp(t1, t3, x3))
    y3int = list(numpy.interp(t1, t3, y3))
    for i in range(n):
        errorx.append(x3int[i] - x1[i])
        errory.append(y3int[i] - y1[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t1, errorx, "red", label="Жертвы")
    plt.plot(t1, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('разница_методов4')
    plt.savefig('разница_методов4')
    plt.show()


    errorx = []
    errory = []
    xint = list(numpy.interp(t1, t, x))
    yint = list(numpy.interp(t1, t, y))
    y1int = list(numpy.interp(t, t1, y1))
    x1int = list(numpy.interp(t, t1, x1))
    for i in range(n):
        errorx.append(xint[i] - x1[i])
        errory.append(yint[i] - y1[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t1, errorx, "red", label="Жертвы")
    plt.plot(t1, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('разница_методов')
    plt.savefig('разница_методов')
    plt.show()
    errorx.clear()
    errory.clear()
    for i in range(n):
        errorx.append(x[i] - x1int[i])
        errory.append(y[i] - y1int[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('разница_методов2')
    plt.savefig('разница_методов2')
    plt.show()
    print(t[-1], t1[-1])

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
    A = ax
    B = -1 * (beta * gamma * ay) / (delta * math.sqrt(alpha * gamma))
    A1 = ay
    B1 = (delta * alpha * ax) / (beta * math.sqrt(alpha * gamma))
    omega = math.sqrt(alpha * gamma)
    t2 = []
    i = 0
    for j in range(n):
        x2.append(A * math.cos(omega * i) + B * math.sin(omega * i))
        y2.append(A1 * math.cos(omega * i) + B1 * math.sin(omega * i))
        t2.append(i)
        i += 1e-8
    print(len(x2), len(t2))
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t2, x2, "red", label="Жертвы")
    plt.plot(t2, y2, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('осциллятор')
    plt.savefig('oscillator')
    plt.show()

    x2int = list(numpy.interp(t, t2, x2))
    y2int = list(numpy.interp(t, t2, y2))
    errorx = []
    errory = []
    amplx = max(x) - max(x2int)
    amply = max(y) - max(y2int)
    for i in range(len(x)):
        errorx.append(x[i] - amplx - x2int[i])
        errory.append(y[i] - amply - y2int[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t, errorx, "red", label="Жертвы")
    plt.plot(t, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('ошибка1')
    plt.savefig('ошибка1')
    plt.show()


    errorx.clear()
    errory.clear()
    x2int = list(numpy.interp(t1, t2, x2))
    y2int = list(numpy.interp(t1, t2, y2))
    amplx = max(x1) - max(x2int)
    amply = max(y1) - max(y2int)
    for i in range(len(x)):
        errorx.append(x1[i] - amplx - x2int[i])
        errory.append(y1[i] - amply - y2int[i])
    plt.xlabel("Время")
    plt.ylabel("ошибка")
    plt.plot(t1, errorx, "red", label="Жертвы")
    plt.plot(t1, errory, "blue", label="Хищники")
    plt.legend(loc='best')
    plt.title('ошибка2')
    plt.savefig('ошибка2')
    plt.show()
