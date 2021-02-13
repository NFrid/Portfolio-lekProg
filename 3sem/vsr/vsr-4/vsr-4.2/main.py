# ВСР 4.2. Задание: разработать программу для считывания данных из
# JSON-файла и вывода их в табличном виде на экран и протестировать
# работоспособность с использованием unittest.


import json


def listToLine(lists: list) -> str:
    res = list()
    for l in lists:
        res.append(list(map(lambda x: str(x).center(30, ' '), l)))
    res = list(map(lambda x: '|'.join(x) + '\n' + '-' * len('|'.join(x)), res))
    res = '\n'.join(res)
    return res


def makeTable(dcts: list) -> str:
    table = list()
    first = list(dcts[0].keys())
    table.append(first)
    for i in range(0, len(dcts)):
        table.append(list(dcts[i].values()))
    return listToLine(table)


def load():
    with open('file.json') as file:
        dicts = json.loads(''.join(file.readlines()))
    return dicts


def main():
    dics = load()
    table = makeTable(dics)
    print(table)


if __name__ == '__main__':
    main()
