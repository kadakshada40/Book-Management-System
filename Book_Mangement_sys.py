class Book:
    # Constructor to initialize book details
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Method to display book details
    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

# List to store multiple books
library = []

# Adding books
library.append(Book("The Alchemist", "Paulo Coelho"))
library.append(Book("Atomic Habits", "James Clear"))

# Display all books
for book in library:
    book.display()
