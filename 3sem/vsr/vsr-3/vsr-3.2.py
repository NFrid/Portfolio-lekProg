# ВСР 3.2. Задание: реализовать программу шифрующую строку, задава-
# емую пользователем, с помощью алгоритма шифрования, использующего
# сдвиг на определенное количество знаков (шифр Цезаря). Сдвиг
# задается пользователем.


def caesar(shift, text):
    res = ''
    for i in text:
        if 'a' <= i <= 'z':
            x = chr((ord(i) + shift - ord('a')) % 26 + ord('a'))
            res += x
        elif 'A' <= i <= 'Z':
            x = chr((ord(i) + shift - ord('A')) % 26 + ord('A'))
            res += x
        elif 'а' <= i <= 'я':
            x = chr((ord(i) + shift - ord('а')) % 30 + ord('а'))
            res += x
        elif 'А' <= i <= 'Я':
            x = chr((ord(i) + shift - ord('А')) % 30 + ord('А'))
            res += x
        else:
            res += i
    return res


def main():
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    print("Encrypted text: ", caesar(shift, text))


if __name__ == "__main__":
    main()
