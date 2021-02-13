# Задание: переписать лямбда-функцию, генерирующую квадраты чисел из
# переменной типа list, через генератор списка.


def rng(n, max):
    import random as r
    return [r.randint(0, max) for i in range(n)]


def main():
    max = int(input("Enter range (max value) for random number generator: "))
    n = int(input("Enter number of random numbers: "))
    rand = rng(n, max)
    print("Generated numbers:", rand)
    print("Squares of them (using lambda):", list(map(lambda x: x * x, rand)))


if __name__ == "__main__":
    main()
