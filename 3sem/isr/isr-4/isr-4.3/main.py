# ИСР 4.3. Задание: дополнить программу задания 4.1, 4.2 тестами с
# использованием пакета py.test.

import pytest
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


def test_json_table():
    assert json_table([{"id": 1, "first_name": "Susann", "last_name": "Wyldish", "email": "swyldish0@bing.com",
                        "gender": "Female", "ip_address": "112.109.35.15"},
                       {"id": 2, "first_name": "Oliy", "last_name": "Bruton", "email": "obruton1@forbes.com",
                        "gender": "Female", "ip_address": "166.20.188.54"},
                       {"id": 3, "first_name": "Ginelle", "last_name": "Inkpen", "email": "ginkpen2@tinypic.com",
                        "gender": "Female", "ip_address": "208.129.167.239"}]) == [
        '---------------------------------------------------------------------------------------------------',
        '| id  | first_name |    last_name    |             email              | gender |    ip_address    |',
        '---------------------------------------------------------------------------------------------------',
        '|  1  |   Susann   |     Wyldish     |       swyldish0@bing.com       | Female |  112.109.35.15   |',
        '|  2  |    Oliy    |     Bruton      |      obruton1@forbes.com       | Female |  166.20.188.54   |',
        '|  3  |  Gnelle   |     Inkpen      |      ginkpen2@tinypic.com      | Female | 208.129.167.239  |',
        '---------------------------------------------------------------------------------------------------']
    # Changed Ginelle to Gnelle for testing purposes


def main():
    test_json_table()


if __name__ == "__main__":
    main()
