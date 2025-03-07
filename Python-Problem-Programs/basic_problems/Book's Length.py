class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages."

    def is_long(self, threshold=300):
        return self.pages > threshold


books = []
num_books = int(input("How many books do you want to enter? "))

for i in range(num_books):
    print(f"\nEnter details for book {i + 1}:")
    title = input("Title: ")
    author = input("Author: ")
    pages = int(input("Number of pages: "))

    book = Book(title, author, pages)
    books.append(book)

print("\nBook Details and Length Check:")

for book in books:
    print(book.describe())
    if book.is_long():
        print("This is a long book.")
    else:
        print("This is a short book.")

