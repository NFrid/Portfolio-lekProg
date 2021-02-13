# ИСР 2.3. Задание: отрефакторить программу с декоратором-модулем
# functools и использовать его функционал.


import functools


def histWrite(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        hist = func(*args, **kwargs)
        try:
            with open("log.txt", "a") as f:
                f.write(hist)
        except IOError as e:
            print(e)
        except:
            print("An unhandled error occurred while writing history to the file.")
    return inner


@histWrite
def main():
    hist = ""
    run = True
    h = "Enter a command: an equation like '2 + 2' (USE SPACES), 'h'/'help' to see this message again or 'q'/'quit' to exit this program.."
    print(h)
    while run:
        cmd = input("> ").lower()
        if cmd == "q" or cmd == "quit":
            print("Quitting...")
            run = False
        elif cmd == "h" or cmd == "help":
            print(h)
        else:
            try:
                res = False
                [a, op, b] = cmd.split()
                a, b = int(a), int(b)
                if op == "+":
                    res = a + b
                elif op == "-":
                    res = a - b
                elif op == "*":
                    res = a * b
                elif op == "/":
                    res = a / b
                else:
                    print("Error: Unknown operand!")

                if res:
                    print("= ", res)
                    hist += cmd + " = " + str(res) + "\n"
            except ValueError:
                print("Error: Wrong command! Type 'h' for help!")

    return hist


if __name__ == "__main__":
    main()
