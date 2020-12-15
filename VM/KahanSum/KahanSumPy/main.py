def KahanSum(arr):
    res = 0.0
    error = 0.0
    for i in range(len(arr)):
        numb = arr[i] - error
        current = res + numb
        error = (current - res) - numb
        res = current
    return res


if __name__ == "__main__":
    print("Введите количество элементов двойной точности")
    n = int(input())
    arr = []
    for i in range(n):
        print("Введите ", i + 1, " элемент")
        arr.append(float(input()))
    print(KahanSum(arr))

