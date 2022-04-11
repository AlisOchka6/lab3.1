class HomeLib(object):
    def __init__(self):
        self.listLib = []

    def __contains__(self, book):
        return book in self.listLib

    def __len__(self):
        return len(self.listLib)

    class Book(object):
        def __init__(self, name, author, year):
            self.name = name
            self.author = author
            self.year = year

        def __contains__(self, attr):
            return attr in {self.name, self.author, self.year}

        def show_book(self):
            print(f"Название: {self.name}")
            print(f"Автор: {self.author}")
            print(f"Год издания: {self.year}\n")

    def add(self, name, author, year):
        self.listLib.append(self.Book(name, author, year))

    def search(self, name):
        for book in self.listLib:
            if name in book:
                book.show_book()
                return book

    def delete(self, book):
        while True:
            if book in self.listLib:
                self.listLib.remove(book)
            else:
                return

    def sort(self, flag):
        if flag == "название":
            list.sort(self.listLib, key=lambda book: book.name)
        if flag == "автор":
            list.sort(self.listLib, key=lambda book: book.author)
        if flag == "год":
            list.sort(self.listLib, key=lambda book: book.year)

    def show(self):
        for book in self.listLib:
            print(f"Название: {book.name}")
            print(f"Автор: {book.author}")
            print(f"Год издания: {book.year}\n")


def main():
    library = HomeLib()
    library.add("Повелитель мух", "Голдинг Уильям", "1954")
    library.add("1984", "Оруэлл Джордж", "1949")
    library.add("Мы", "Замятин Евгений", "1920")
    library.add("О дивный новый мир", "Хаксли Олдос", "1932")
    library.add("451 градус по Фаренгейту", "Брэдбери Рэй", "1953")

    while True:
        try:
            work = int(input(
                "Введите 1, если хотите увидеть список книг в библиотеке!\nВведите 2, если хотите добавить книгу в "
                "библиотеку!\nВведите 3, если хотите отсортировать книгу по какому-то полю!\nВведите 4, "
                "если хотите удалить книгу из библиотеки!\nВведите 5, если хотите найти книгу в библиотеке!\nДля "
                "выхода нажмите любую клавишу!\n"))
            if work == 1:
                library.show()
            elif work == 2:
                name = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издательства книги: ")
                library.add(name, author, year)
            elif work == 3:
                flag = input(
                    "Введите параметр, по которому вы хотите отсортировать библиотеку (название, автор, год): ")
                library.sort(flag)
                library.show()
            elif work == 4:
                attr = input(
                    "Введите название, автора или год издательства книги, которую вы хотите удалить: ")
                library.delete(library.search(attr))
            elif work == 5:
                attr = input("Введите название, автора или год издательства книги : ")
                library.search(attr)
            else:
                break
        except ValueError:
            break


if __name__ == "__main__":
    main()
