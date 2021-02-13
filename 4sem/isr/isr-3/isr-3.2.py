# ИСР 3.2. Задание: создать геттеры и сеттеры для классов «запись»,
# «комментарий» приложения «Гостевая книга», а также функции для
# вывода на печать информации, хранящийся в объектах.


class Post:
    def __init__(self, author, content):
        self.__author = author
        self.__content = content

    @property
    def author(self):
        return self.__author

    @author.getter
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author == str(value)

    @property
    def content(self):
        return self.__content

    @content.getter
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content == str(value)

    def show(self):
        print(f'By: {self.author}\n\n{self.content}\n')


class Comment(Post):
    def show(self):
        print(f'{self.author}: {self.content}\n')


def main():
    post = Post(
        "John Doe",
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.",
    )
    comment = Comment("minecraft123", "wowee!")
    comment2 = Comment("shrek", "dis sucks")

    post.show()
    comment.show()
    comment2.show()


if __name__ == "__main__":
    main()
