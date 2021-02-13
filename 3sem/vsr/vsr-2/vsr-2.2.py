# Задание: разработать программу, которая для заданного количества
# значений возвращала бы список из уникальных элементов,
# содержащихся во входном наборе значений.


def uniq(vals):
    return list(set(vals))


def main():
    vals: list = input("Enter values separated by '|' sign:\n> ").split("|")
    print("Answer:", "".join(" " + str(v) + " |" for v in uniq(vals)))


if __name__ == "__main__":
    main()
