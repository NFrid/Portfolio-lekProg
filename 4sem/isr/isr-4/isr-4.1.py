# ИСР 4.1. Задание: создать программу по заполнению массива
# случайными значениями. Сортировка значений в списке методом
# вставки, плавной сортировки, с помощью встроенных функций языка.


def insertS(arr):
    for i in range(len(arr)):
        j = i - 1
        key = arr[i]
        while arr[j] > key and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def smoothS(nums):
    def downHeap(nums, k, n):
        newE = nums[k]
        while 2 * k + 1 < n:
            child = 2 * k + 1
            if child + 1 < n and nums[child] < nums[child + 1]:
                child += 1
            if newE >= nums[child]:
                break
            nums[k] = nums[child]
            k = child
        nums[k] = newE
    size = len(nums)
    for i in range(size // 2 - 1, -1, -1):
        downHeap(nums, i, size)
    for i in range(size - 1, 0, -1):
        temp = nums[i]
        nums[i] = nums[0]
        nums[0] = temp
        downHeap(nums, 0, i)
    return nums


def randArray():
    import numpy as np
    return np.random.randint(0, 20, 10)


def main():
    arr = randArray()
    print(f'''
Исходный массив: {arr}

Методом вставки: {insertS(arr)}

Методом плавной сортировки: {smoothS(arr)}

Встроенными функциями языка: {sorted(arr)}
          ''')


if __name__ == "__main__":
    main()
