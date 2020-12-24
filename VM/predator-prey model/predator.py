import math
def runge_kutta_method(eq, f, a, b, h):
    k1 = h * f(eq[0], eq[1], a, b)
    k2 = h * f(eq[0] + h / 2.0, eq[1] + k1 * h / 2.0, a, b)
    k3 = h * f(eq[0] + h / 2.0, eq[1] + k2 * h / 2.0, a, b)
    k4 = h * f(eq[0] * h, eq[1] + k3 * h, a, b)
    return (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0


def Bogacki_Shampine_method(eq, f, f1, a, b, c, d, h):
    k1 = h * f(eq[0], eq[1], a, b)
    q1 = h * f1(eq[0], eq[1], c, d)

    k2 = h * f(eq[0] + k1 * h / 2.0, eq[1] + q1 * h / 2.0, a, b)
    q2 = h * f1(eq[0] + k1 * h / 2.0, eq[1] + q1 * h / 2.0, c, d)

    k3 = h * f(eq[0] + k2 * h * 3 / 2.0, eq[1] + q2 * h * 3 / 2.0, a, b)
    q3 = h * f1(eq[0] + k2 * h * 3 / 2.0, eq[1] + q2 * h * 3 / 2.0, c, d)

    x = eq[0] + (2/9.0) * h * k1 + h*k2/3.0 + (4/9.0)*h*k3
    y = eq[1] + (2/9.0) * h * q1 + h*q2/3.0 + (4/9.0)*h*q3


    k4 = h * f(x , y, a, b)
    q4 = h * f1(x, y, c, d)

    res = []
    res.append(eq[0] + (7/24.0)*h*k1 + h*k2/4.0 + h*k3/3.0 + h*k4/8.0)
    res.append(eq[1] + (7/24.0)*h*q1 + h*q2/4.0 + h*q3/3.0 + h*q4/8.0)

    return res


def foo(eq, f, f1, a, b, c, d, h):
    k1 = h * f(eq[0], eq[1], a, b)
    q1 = h * f1(eq[0], eq[1], c, d)

    k2 = h * f(eq[0] + k1 / 2.0, eq[1] + q1 / 2.0, a, b)
    q2 = h * f1(eq[0] + k1 / 2.0, eq[1] + q1 / 2.0, c, d)

    k3 = h * f(eq[0] + k2 / 2.0, eq[1] + q2 / 2.0, a, b)
    q3 = h * f1(eq[0] + k2 / 2.0, eq[1] + q2 / 2.0, c, d)

    k4 = h * f(eq[0] + k3, eq[1] + q3, a, b)
    q4 = h * f1(eq[0] + k3, eq[1] + q3, c, d)

    res = []
    res.append(eq[0] + ((k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0))
    res.append(eq[1] + ((q1 + 2.0 * q2 + 2.0 * q3 + q4) / 6.0))
    return res

def Adams(eq, f, f1, a, b, c, d, h):
    x1 = eq[0] + h*f(eq[0], eq[1], a, b)
    y1 = eq[1] + h * f1(eq[0], eq[1], c, d)

    x2 = x1 + h*(3*f(x1, y1, a, b)/2.0 - f(eq[0], eq[1], a, b)/2.0)
    y2 = y1 + h*(3*f1(x1, y1, c, d)/2.0 - f1(eq[0], eq[1], c, d)/2.0)

    x3 = x2 + h*(23*f(x2, y2, a, b)/12.0 - 4*f(x1, y1, a, b)/3.0 + 5*f(eq[0], eq[1], a, b)/12.0)
    y3 = y2 + h*(23*f1(x2, y2, c, d)/12.0 - 4*f1(x1, y1, c, d)/3.0 + 5*f1(eq[0], eq[1], c, d)/12.0)

    x4 = x3 + h*(55*f(x3, y3, a, b)/24.0 - 59*f(x2, y2, a, b)/24.0 + 37*f(x1, y1, a, b)/24.0 - 3*f(eq[0], eq[1], a, b)/8.0)
    y4 = y3 + h*(55*f1(x3, y3, c, d)/24.0 - 59*f1(x2, y2, c, d)/24.0 + 37*f1(x1, y1, c, d)/24.0 - 3*f1(eq[0], eq[1], c, d)/8.0)

    x5 = x4 + h*(1901*f(x4, y4, a, b)/720.0 - 1387*f(x3, y3, a, b)/360.0 + 109*f(x2, y2, a, b)/30.0 - 637*f(x1, y1, a, b)/360.0 + 251*f(eq[0], eq[1], a, b)/720.0)
    y5 = y4 + h*(1901*f1(x4, y4, c, d)/720.0 - 1387*f1(x3, y3, c, d)/360.0 + 109*f1(x2, y2, c, d)/30.0 - 637*f1(x1, y1, c, d)/360.0 + 251*f1(eq[0], eq[1], c, d)/720.0)

    res = [x5, y5]
    return res

