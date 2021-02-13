# ИСР 1.2. Задание: разработать скрипт, вычисляющий сумму первых
# n-членов арифметической прогрессии (использовать функции, условные операторы).

# Прогрессия от 1 с шагом 1.


def asum(n):
    return sum(list(range(n + 1))) if n >= 0 else "NULL - No negative range allowed!!"


def main():
    print("Enter the range:\n> ", end="")
    n = int(input())
    print("Answer:", asum(n))


if __name__ == "__main__":
    main()
