# ИСР 3.1. Задание: разработать классы и объекты «запись»,
# «комментарий» для приложения «Блог» (используя наследование).


class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content

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
