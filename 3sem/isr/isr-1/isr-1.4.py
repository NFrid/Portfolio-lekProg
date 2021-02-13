# ИСР 1.4. Задание: создать сценарий, вычисляющий операции
# сложения, вычитания, умножения, деления для двух операндов.


def main():
    print("Enter two numbers:")
    a, b = float(input("a = ")), float(input("b = "))

    print("a + b = ", a + b)
    print("a - b = ", a - b)
    print("a * b = ", a * b)
    print("a / b = ", a / b)


if __name__ == "__main__":
    main()
