# ВСР 1.1. Задание: разработать фрагмент программы, который будет
# сохранять вводимые пользователем данные, по выбору в json, или csv-
# файле (использовать модули csv, json) с использованием протокола
# менеджеров контекста, а также расширенного синтаксиса исключений.


def writeJson(*data):
    try:
        with open("file.json", "w") as f:
            import json
            try:
                json.dump(data, f, sort_keys=True, indent=2)
                print("Done!")
            except json.JSONDecodeError as e:
                print(e)
                return None
    except FileNotFoundError as e:
        print(e)
        return None


def main():
    data = []
    n = input("How many items would you enter?\n> ")
    for i in range(int(n)):
        data.append({"name": input(str(i) + ". Name: "),
                     "count": input(str(i) + ". Count: ")})
    writeJson(data)


if __name__ == "__main__":
    main()
