import json

library = []

# Load library data from file library.txt (if exists)
def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)  # Convert JSON data to list
    except (FileNotFoundError, json.JSONDecodeError):
        library = []

# Save library data to file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file, indent=4)  # Convert list to JSON and save

def add_book():
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }

    library.append(book)
    print("Book added successfully!")
    save_library()  # Save updated library

def remove_book():
    title = input("Enter book title to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            save_library()  # Save updated library
            return
    print("Book not found!")

def search_book():
    search_query = input("Enter title or author to search: ").lower()
    results = [book for book in library if search_query in book["title"].lower() or search_query in book["author"].lower()]
    
    if results:
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    else:
        print("No matching books found!")

def display_books():
    if not library:
        print("Library is empty!")
        return
    for book in library:
        print(f"{book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")

def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Percentage read: {read_percentage:.2f}%")

# Load library at the start
load_library()

while True:
    print("\nWelcome to Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))  # Input ko int mai convert kiya
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 6.")
        continue  # Galat input pe loop dobara chalega

    if choice == 1:
        add_book()
    elif choice == 2:
        remove_book()
    elif choice == 3:
        search_book()
    elif choice == 4:
        display_books()
    elif choice == 5:
        display_statistics()
    elif choice == 6:
        print("Saving library and exiting... 📂")
        save_library()  # Ensure saving before exiting
        break
    else:
        print("Invalid choice, please try again.")
