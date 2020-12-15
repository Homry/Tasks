def runge_kutta_method(eq, f, a, b, h):
    k1 = h * f(eq[0], eq[1], a, b)
    k2 = h * f(eq[0] + h / 2.0, eq[1] + k1 * h / 2.0, a, b)
    k3 = h * f(eq[0] + h / 2.0, eq[1] + k2 * h / 2.0, a, b)
    k4 = h * f(eq[0] * h, eq[1] + k3 * h, a, b)
    return (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

def Bogacki_Shampine_method(eq, f, a, b, h):
    k1 = f(eq[0], eq[1], a, b)
    k2 = f(eq[0] + h / 2.0, eq[1] + k1 * h / 2.0, a, b)
    k3 = f(eq[0] + 3*h/4.0, eq[1] + 3*h*k2/4.0, a, b)
    y = eq[1] + 2 * h * k1 / 24.0 + h * k2 / 4.0 + 4*h*k3/9.0
    k4 = f(eq[0]+h, y, a, b)
    return 7*h*k1/24.0 + h*k2/4.0 + h*k3/3.0 + h*k4/8.0