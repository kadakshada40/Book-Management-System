
# Book Management System

A simple Python script to manage a list of books by defining a `Book` class and displaying book details.

## Features
- Defines a `Book` class with `title` and `author` attributes.
- Implements a `display` method to print book details.
- Creates a `library` list to store multiple books.
- Demonstrates adding sample books and displaying all entries.

## Getting Started

### Prerequisites
- Python 3.x installed on your system.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/book-management-system.git
    cd book-management-system
    ```
2. Ensure you have Python 3 installed:
    ```bash
    python3 --version
    ```

## Usage
1. Open the script file:
    ```bash
    nano Book_Mangement_sys.py
    ```
2. Run the script:
    ```bash
    python3 Book_Mangement_sys.py
    ```
3. You should see output similar to:
    ```
    Title: The Alchemist, Author: Paulo Coelho
    Title: Atomic Habits, Author: James Clear
    ```

## Code Overview

```python
class Book:
    """
    A class to represent a book with title and author.
    """

    def __init__(self, title, author):
        """
        Initialize a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def display(self):
        """
        Display the book's details.
        """
        print(f"Title: {self.title}, Author: {self.author}")

# List to store multiple books
library = []

# Sample books
library.append(Book("The Alchemist", "Paulo Coelho"))
library.append(Book("Atomic Habits", "James Clear"))

# Display all books
for book in library:
    book.display()
```

