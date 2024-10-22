class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Creating an object of the Book class
book1 = Book("1984", "George Orwell")
print(f"Title: {book1.title}, Author: {book1.author}")
