# Задание: реализовать программу шифрующую строку, задаваемую
# пользователем, с помощью алгоритма шифрования ROT13.


def rot13(letter):
    if ord("a") + 13 > ord(letter) >= ord("a"):
        return chr(ord(letter) + 13)
    elif ord("z") >= ord(letter) >= ord("a") + 13:
        return chr(ord(letter) - 13)
    else:
        return letter


def main():
    text_to_encrypt = input("Enter text to encrypt: ")
    cipher_text = "".join(list(map(rot13, text_to_encrypt)))
    print("Encrypted text:", cipher_text)


if __name__ == "__main__":
    main()
