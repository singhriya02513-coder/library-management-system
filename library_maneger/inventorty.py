import json
import logging
import book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def _init_(self, file_path="library_data.json"):
        self.file_path = file_path
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Added book: {book.title}")

    def search_by_title(self, title):
        return [b for b in self.books if b.title.lower() == title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        return self.books

    def save_data(self):
        try:
            with open(self.file_path, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
            logging.info("Saved library data.")
        except Exception as e:
            logging.error(f"Error while saving data: {e}")

    def load_data(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.books = [book.Book(**d) for d in data]
            logging.info("Loaded library data.")
        except FileNotFoundError:
            logging.warning("Data file not found. Starting with empty library.")
            self.books = []
        except Exception as e:
            logging.error(f"Corrupted file. Starting empty. Error: {e}")
            self.books = []
