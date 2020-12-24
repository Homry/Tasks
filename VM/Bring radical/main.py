import math


def Newton(left, right, a, eps):
    if (left * left * left * left * left + left + a) * (right * right * right * right * right + right + a) > 0:
        print("Корня не существует")
        return 0

    if ((left * left * left * left * left + left + a) * (20 * left * left * left)) > 0:
        x0 = left
    else:
        x0 = right
    approx = x0 - (x0 * x0 * x0 * x0 * x0 + x0 + a) / (5 * x0 * x0 * x0 * x0 + 1)
    i = 0

    while math.fabs(x0 - approx) > eps:
        print(i, 'iteration', approx)
        x0 = approx
        approx = x0 - (x0 * x0 * x0 * x0 * x0 + x0 + a) / (5 * x0 * x0 * x0 * x0 + 1)
        i+=1
    return approx


def Bisection(left, right, a, eps):
    if (left * left * left * left * left + left + a) * (right * right * right * right * right + right + a) > 0:
        print("Корня не существует")
        return 0
    mid = left + (right - left) / 2.0
    i = 0
    while (right - left > eps):
        print(i, 'iteration', mid)
        if (left * left * left * left * left + left + a) * (mid * mid * mid * mid * mid + mid + a) <= 0:
            right = mid
        else:
            left = mid
        mid = left + (right - left) / 2.0
        i+=1
    return mid


if __name__ == '__main__':
    print("Введите левую границу")
    left = float(input())
    print("Введите правую границу")
    right = float(input())
    print("Введите константу a для уравнения Бринга")
    a = float(input())
    print("Введите точность")
    epsilon = float(input())
    print("Newton")
    x = Newton(left, right, a, epsilon)
    print(x)
    print("x^5+x+a = ", x * x * x * x * x + x + a)
    print()
    print("Bisection")
    x = Bisection(left, right, a, epsilon)
    print(x)
    print("x^5+x+a = ", x * x * x * x * x + x + a)
