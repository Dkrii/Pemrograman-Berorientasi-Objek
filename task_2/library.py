class Book:
    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            return f"The book '{self.title}' has been borrowed."
        else:
            return f"The book '{self.title}' is currently not available."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"The book '{self.title}' has been returned."
        else:
            return f"The book '{self.title}' was not borrowed."

    def show_info(self):
        status = "available" if self.available else "not available"
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Status: {status}"

# Creating a book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
print(book1.borrow_book())  # Output: The book 'The Great Gatsby' has been borrowed.
print(book1.borrow_book())  # Output: The book 'The Great Gatsby' is currently not available.
print(book1.return_book())  # Output: The book 'The Great Gatsby' has been returned.
print(book1.return_book())  # Output: The book 'The Great Gatsby' was not borrowed.

books = []

while True:
    print("Menu")
    print("1. List books")
    print("2. Add book")
    print("3. Borrow book")
    print("4. Return book")
    print("5. Exit")

    menu = input("Select menu: ")
    if menu == "1":
        for index, book in enumerate(books):
            print(f"{index} - {book.show_info()}")

    elif menu == "2":
        title = input("Insert title: ")
        author = input("Insert author: ")
        ISBN = input("Insert ISBN: ")
        new_book = Book(title, author, ISBN)
        books.append(new_book)

    elif menu == "3":
        index = int(input("Choose book index: "))
        print(books[index].borrow_book())

    elif menu == "4":
        index = int(input("Choose book index: "))
        print(books[index].return_book())

    elif menu == "5":
        break