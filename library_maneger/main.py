
from book import Book
from inventorty import LibraryInventory

def menu():
    lib = LibraryInventory()

    while True:
        print("\n----- Library Menu -----")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")

                lib.add_book(Book(title, author, isbn))
                print("Book added.")

            elif choice == "2":
                isbn = input("ISBN to issue: ")
                book = lib.search_by_isbn(isbn)
                if book and book.issue():
                    print("Book issued.")
                else:
                    print("Cannot issue book.")

            elif choice == "3":
                isbn = input("ISBN to return: ")
                book = lib.search_by_isbn(isbn)
                if book and book.return_book():
                    print("Book returned.")
                else:
                    print("Cannot return book.")

            elif choice == "4":
                for b in lib.display_all():
                    print(b)

            elif choice == "5":
                title = input("Title: ")
                results = lib.search_by_title(title)
                for b in results:
                    print(b)

            elif choice == "6":
                lib.save_data()
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Try again.")

        except Exception as e:
            print("Error:", e)

if __name__ == "_main_":
    menu()

