# ИСР 4.1. Задание: разработать программу для считывания данных JSON-
# формата из файла и вывод их в табличном виде на экран. Организо-
# вать тестирование работоспособности программы с помощью assert,
# print.


import json


def json_table(data):
    table = []
    string = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
    t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id', 'first_name', 'last_name', 'email',
                                                                               'gender', 'ip_address')
    header = '-' * len(t_caption)

    table.append(header)
    table.append(t_caption)
    table.append(header)

    for element in range(len(data)):
        temp = data[element]
        res = string.format(**temp)
        table.append(res)
    table.append(header)
    return table


def test_function(function, arg):
    try:
        assert function(arg)[1
                             ] == '| id  | first_name |    last_name    |             email              | gender |    ip_address    |'
    except:
        print("FAILED: Expected different header")
    try:
        assert type(function(arg)) is list
    except:
        print("FAILED: Wrong type -", type(function(arg)))
    try:
        assert len(function(arg)) == 104  # + 4 for --- and header
    except:
        print("FAILED: Expected different length -",
              len(function(arg)))


def main():
    with open('file.json') as f:
        data_dict = json.load(f)

    test_function(json_table, data_dict)
    for item in json_table(data_dict):
        print(item)


if __name__ == "__main__":
    main()
