# ИСР 1.3. Задание: разработать скрипт, позволяющий вычислить площадь
# треугольника с помощью формулы Герона.


def S(a, b, c):
    p = (a + b + c) / 2
    return (p * (p-a) * (p-b) * (p-c)) ** (1/2)


def main():
    print("Enter sizes of the triangle:")
    a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
    if (a > 0) and (b > 0) and (c > 0):
        print("Answer:", str(S(a, b, c)))
    else:
        print("Error: Invalid tirangle!!")


if __name__ == "__main__":
    main()
