# ИСР 2.1. Задание: разработать прототип программы «Калькулятор»,
# позволяющую выполнять базовые арифметические действия и функцию
# обертку, сохраняющую название выполняемой операции, аргументы и
# результат в файл (без использования '@').


def histWrite(hist):
    try:
        with open("log.txt", "a") as f:
            f.write(hist)
    except IOError as e:
        print(e)
    except:
        print("An unhandled error occurred while writing history to the file.")


def main():
    hist = ""
    run = True
    h = "Enter a command: an equation like '2 + 2' (USE SPACES), 'h'/'help' to see this message again or 'q'/'quit' to exit this program.."
    print(h)
    while run:
        cmd = input("> ").lower()
        if cmd == "q" or cmd == "quit":
            print("Quitting...")
            histWrite(hist)
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


if __name__ == "__main__":
    main()
