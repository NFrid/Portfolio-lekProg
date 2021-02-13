# ИСР 1.3. Задание: дополнить программу для считывания данных с
# использованием менеджера контекстов и реализацией расширенного
# синтаксиса для обработки исключений.


import json


def fileToJson(file):
    try:
        with open(file) as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e)
        exit(1)
    finally:
        # idk what to put here but I need to use finally so...
        print("\nYo file loading stage is over! Here's meme for ya!\n---------------\nFinland + Italy\n---------------\n    Finally\n<bruh w/ test tube>\n    Finaly\n---------------")


def jsonToTable(data):
    res = []
    record = "| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |"
    head = "| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |".format(
        "id", "first_name", "last_name", "email", "gender", "ip_address"
    )
    line = "=" * len(head)

    res.append(line)
    res.append(head)
    res.append(line)
    for el in range(len(data)):
        res.append(record.format(**data[el]))
    res.append(line)
    return res


def main():
    # still fil instead of file !!!!
    a = jsonToTable(fileToJson("fil.json"))
    for el in a:
        print(el)


if __name__ == "__main__":
    main()
