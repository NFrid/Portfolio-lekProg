# ИСР 3.2. Задание: разработайте сценарий с реализацией операции
# поиска подстроки в тексте.


def all_occurrences(search_string, what_to_find):
    occurrence = search_string.find(what_to_find)
    if occurrence != -1:
        print("First substring occurrence:", occurrence)
    else:
        print("No substring occurrences found!!")

    length_search_string = len(search_string)
    length_what_to_find = len(what_to_find)
    while occurrence != -1:
        occurrence = search_string.find(what_to_find, occurrence +
                                        length_what_to_find,
                                        length_search_string)
        if occurrence != -1:
            print("Substring occurrence:", occurrence)
        else:
            print("No more substring occurrences found!!")


def main():
    search_string = input("Enter a string: ")
    what_to_find = input("Enter a substring to find: ")
    all_occurrences(search_string, what_to_find)


if __name__ == "__main__":
    main()
