# Вариант 8

# Найдите площадь поверхности прямой призмы, в основании которой лежит ромб
# с диагоналями, равными d1 и d2, и боковым ребром, равным h.
# Решение задачи оформите в виде функции square(d1,d2,h) которая возвращает
# значение переменной s. Например, при d1=6; d2=8; h=10 функция square(6,8,10)
# вернет s=248


import math


def square(d1, d2, h):
    return 4*math.sqrt((d1/2)**2 + (d2/2)**2)*h + d1*d2


def main():
    print("Enter sizes of the prism:")
    d1, d2, h = float(input("d1 = ")), float(
        input("d2 = ")), float(input("h = "))
    print("Answer:", square(d1, d2, h))


if __name__ == "__main__":
    main()
