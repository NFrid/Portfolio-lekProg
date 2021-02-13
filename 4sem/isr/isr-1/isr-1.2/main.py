# ИСР 1.2. Дополнение программы для считывания данных проверкой утверждений или
# высказываний(assert). Создание отдельного блока для такой проверки(с помощью
# __name__) и скрипта командной строки для запуска этих проверок.


import json


def fileToJson(file):
    try:
        with open(file) as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(e)
        exit(1)


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
    # Renamed file.json to fil.json for test
    a = jsonToTable(fileToJson("fil.json"))
    for el in a:
        print(el)


if __name__ == "__main__":
    main()
