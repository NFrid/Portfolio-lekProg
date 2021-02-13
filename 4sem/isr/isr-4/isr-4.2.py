# ИСР 4.2. Задание: создать программу по распределению списка со
# случайными значениями на два списка по определенному критерию
# (четность/нечетность, положительные/отрицательные числа).


def odditySort(arr):
    odd = []
    even = []
    for el in arr:
        if el % 2 != 0:
            odd.append(el)
        else:
            even.append(el)
    return odd, even


def signCheck(arr):
    m = []
    p = []
    for el in arr:
        if el < 0:
            m.append(el)
        else:
            p.append(el)
    return m, p


def randArray():
    import numpy as np
    return np.random.randint(-10, 20, 10)


def main():
    arr = randArray()
    print(f'''
Исходный массив: {arr}

Нечётные, чётные: {odditySort(arr)}

Отрицательные, положительные: {signCheck(arr)}
          ''')


if __name__ == "__main__":
    main()
