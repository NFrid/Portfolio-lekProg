# ИСР 4.2. Задание: дополнить программу задания 4.1 тестами с
# использованием библиотеки doctest.

import json


def json_table():
    """
    >>> json_table()[1]
    '| id   | first_name |    last_name    |             email              | gender |    ip_address    |'
    """
    # Added one wrong space after id to make an error

    with open('file.json') as f:
        data_dict = json.load(f)
    table = []
    string = '| {id:^3} | {first_name:^10} | {last_name:^15} | {email:^30} | {gender:^6} | {ip_address:^16} |'
    t_caption = '| {:^3} | {:^10} | {:^15} | {:^30} | {:^6} | {:^16} |'.format('id', 'first_name', 'last_name', 'email',
                                                                               'gender', 'ip_address')
    header = '-' * len(t_caption)
    table.append(header)
    table.append(t_caption)
    table.append(header)
    for element in range(len(data_dict)):
        temp = data_dict[element]
        res = string.format(**temp)
        table.append(res)
    table.append(header)
    return table


def main():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    main()
