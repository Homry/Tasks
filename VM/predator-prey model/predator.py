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
