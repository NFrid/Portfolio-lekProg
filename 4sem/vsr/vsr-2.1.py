# ВСР 2. Задание: разработать функцию-декоратор, вычисляющую время
# выполнения декорируемой функции.


from datetime import datetime as d
from functools import wraps


def showtime(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start = d.now()
        f = func()
        print("Done in", d.now() - start)
        return f
    return inner


@showtime
def someUsefulThing():
    switch = False
    for i in range(12345):
        for j in range(12345):
            switch = not switch
    return switch


def main():
    someUsefulThing()


if __name__ == "__main__":
    main()
