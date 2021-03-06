import math

def KahanSum(arr):
    res = 0.0
    error = 0.0
    for i in range(len(arr)):
        numb = arr[i] - error
        current = res + numb
        error = (current - res) - numb
        res = current
    return res

def NeumaierSum(arr):
    res = 0.0
    error = 0.0
    for i in range(len(arr)):
        t = res + arr[i]
        if math.fabs(res) >= math.fabs(arr[i]):
            error += (res - t) + arr[i]
        else:
            error += (arr[i] - t) + res
        res = t
    return res + error

def KleinSum(arr):
    res = 0.0
    cs = 0.0
    ccs = 0.0
    for i in range(len(arr)):
        t = res + arr[i]
        if math.fabs(res) >= math.fabs(arr[i]):
            error = (res - t) + arr[i]
        else:
            error = (arr[i] - t) + res
        res = t
        t = cs + error
        if math.fabs(cs) >= math.fabs(error):
            cc = (cs - t) + error
        else:
            cc = (error - t) + cs
        cs = t
        ccs = ccs + cc
    return res + cs + ccs




if __name__ == "__main__":
    print("Введите количество элементов двойной точности")
    n = int(input())
    arr = []
    for i in range(n):
        print("Введите ", i + 1, " элемент")
        arr.append(float(input()))
    print(KahanSum(arr))



