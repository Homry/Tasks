import numpy
import matplotlib.pyplot as plt

class equations:
    def __init__(self, alpha, betta, gamma, delta, x, y, h):
        self.alpha = alpha
        self.betta = betta
        self.gamma = gamma
        self.delta = delta
        self.currentX = x
        self.currentY = y
        self.h = h
        self.resX = []
        self.resY = []

    def f1(self, x0, y0, alpha, betta):
        return alpha * x0 - betta * x0 * y0

    def f2(self, x0, y0, gamma, delta):
        return -gamma * y0 + delta * x0 * y0


def method(eq):
    for i in range(4000):
        k1 = eq.h * eq.f1(eq.currentX, eq.currentY, eq.alpha, eq.betta)
        q1 = eq.h * eq.f2(eq.currentX, eq.currentY, eq.gamma, eq.delta)

        k2 = eq.h * eq.f1(eq.currentX + eq.h / 2.0, eq.currentY + k1 * eq.h / 2.0, eq.alpha, eq.betta)
        q2 = eq.h * eq.f2(eq.currentX + + eq.h / 2.0, eq.currentY + q1 * eq.h / 2.0, eq.gamma, eq.delta)

        k3 = eq.h * eq.f1(eq.currentX + eq.h / 2.0, eq.currentY + k1 * eq.h / 2.0, eq.alpha, eq.betta)
        q3 = eq.h * eq.f2(eq.currentX + + eq.h / 2.0, eq.currentY + q2 * eq.h / 2.0, eq.gamma, eq.delta)

        k4 = eq.h * eq.f1(eq.currentX + eq.h, eq.currentY + k3 * eq.h, eq.alpha, eq.betta)
        q4 = eq.h * eq.f2(eq.currentX + eq.h, eq.currentY + q3 * eq.h, eq.gamma, eq.delta)

        x = eq.currentX + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        y = eq.currentY + (q1 + 2.0 * q2 + 2.0 * q3 + q4) / 6.0
        eq.resX.append(x)
        eq.resY.append(y)
        eq.currentX = x
        eq.currentY = y



if __name__ == '__main__':
    eq = equations(5, 3, 1, 1, 3, 1, 0.01)

    method(eq)
    t = numpy.linspace(0, 1, 4000)
    plt.xlabel("Время")
    plt.ylabel("Количество особей")
    plt.plot(t, eq.resX, "red", label="Жертвы")
    plt.plot(t, eq.resY, "blue", label="Хищники")
    plt.legend(bbox_to_anchor=(0.97, 0.27))
    plt.show()


