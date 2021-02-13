# ВСР 4. Задание: создать программу с реализацией вручную одного
# из алгоритмов сортировки (вставки, плавной сортировки).


def insertS(arr):
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def randArray():
    import numpy as np
    return np.random.randint(0, 20, 10)


def main():
    arr = randArray()
    print("Исходный массив:", arr)
    print("Метод вставки", insertS(arr))


if __name__ == "__main__":
    main()
