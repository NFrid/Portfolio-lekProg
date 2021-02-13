# ИСР 3.3. Задание: реализовать программу-игру «Угадай число», в
# которой для вывода на экран информации использовать метод format.


def guessGame(a, b):
    print("Starting a new game...\n")
    import random as r
    n = r.randint(a, b)
    u = int(input("Try guess a number: "))
    while n != u:
        print("Too small...") if u < n else print("Too big...")
        u = int(input("Try another time: "))
    retry = input("You win!! Try again? [y/N] ")
    if retry.lower() == 'y':
        res = [int(e) for e in input(
            "Enter new range (empty to use previous - {}..{}):".format(a, b)).split()]
        if len(res) == 2:
            [a, b] = res
        guessGame(a, b)


def main():
    [a, b] = [int(e) for e in input(
        "Enter range of randomness (min max) separated by spaces: ").split()]
    guessGame(a, b)


if __name__ == "__main__":
    main()
