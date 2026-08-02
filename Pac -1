# -----------------------------
# Book Class
# -----------------------------

class Book:

    # Constructor - called automatically when an object is created
    def __init__(self, title, author):

        # Store title of the book
        self.title = title

        # Store author's name
        self.author = author

        # By default every new book is available
        self.available = True


# -----------------------------
# Patron Class
# -----------------------------

class Patron:

    # Constructor
    def __init__(self, name):

        # Store patron name
        self.name = name

        # List to store borrowed books
        self.borrowed_books = []


# -----------------------------
# Library Class
# -----------------------------

class Library:

    # Constructor
    def __init__(self):

        # List to store all books
        self.books = []

        # List to store all registered patrons
        self.patrons = []

    # Add a book to library
    def add_book(self, book):

        self.books.append(book)

        print(book.title, "added successfully.")

    # Register a new patron
    def register_patron(self, patron):

        self.patrons.append(patron)

        print(patron.name, "registered successfully.")

    # Borrow a book
    def borrow_book(self, patron, book):

        # Check whether the book is available
        if book.available:

            # Book is no longer available
            book.available = False

            # Add book to patron's borrowed list
            patron.borrowed_books.append(book)

            print(patron.name, "borrowed", book.title)

        else:

            print(book.title, "is not available.")

    # Return a borrowed book
    def return_book(self, patron, book):

        # Check if the patron has this book
        if book in patron.borrowed_books:

            # Book becomes available again
            book.available = True

            # Remove book from patron list
            patron.borrowed_books.remove(book)

            print(patron.name, "returned", book.title)

        else:

            print("Book was not borrowed by", patron.name)


# -----------------------------
# Main Program
# -----------------------------

# Create Library Object
library = Library()

# Create Book Objects
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Java Programming", "James Gosling")
book3 = Book("C Programming", "Dennis Ritchie")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print()

# Create Patron Objects
patron1 = Patron("Rahul")
patron2 = Patron("Priya")

# Register Patrons
library.register_patron(patron1)
library.register_patron(patron2)

print()

# Borrow Books
library.borrow_book(patron1, book1)
library.borrow_book(patron2, book2)

print()

# Try borrowing an already borrowed book
library.borrow_book(patron2, book1)

print()

# Return Book
library.return_book(patron1, book1)

print()

# Borrow Again
library.borrow_book(patron2, book1)

print()

# Display Final Status
print("-------- Final Status --------")

print("\nBooks Available:")

for book in library.books:

    print(book.title, "-", book.available)

print("\nBorrowed Books:")

for patron in library.patrons:

    print(patron.name, "has borrowed:")

    if len(patron.borrowed_books) == 0:

        print("No books")

    else:

        for book in patron.borrowed_books:

            print(book.title)