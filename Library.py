class Book:
    def __init__(self, title, author): 
        self.title = title 
        self.author = author 
        self.is_borrowed = False
        
    def __str__(self):
        # Fix: Improved book status display.
        return f"Book: {self.title} by {self.author}. {'Currently borrowed' if self.is_borrowed else 'Available'}"
        
class Library: 
    def __init__(self): 
        self.books = [] # List of books in the library
            
    def add_book(self, title, author):  # Fix: Changed method name to singular for consistency
        book = Book(title, author)
        self.books.append(book)
        print(f"The book '{title}' by {author} has been added to the library.")
            
    def borrow_book(self, title):  
        for book in self.books: 
            if book.title == title and not book.is_borrowed:  # Fix: Corrected borrowing logic
                book.is_borrowed = True 
                print(f"The book '{title}' is now borrowed.")
                return
        print(f"The book '{title}' is either borrowed or not in the library.")
                    
    def return_book(self, title):  
        for book in self.books: 
            if book.title == title and book.is_borrowed:  # Fix: Corrected return logic
                book.is_borrowed = False
                print(f"The book '{title}' has been returned.")
                return
        print(f"The book '{title}' was not borrowed or does not exist in the library.")
    
    def view_books(self): 
        if not self.books:  # Fix: Improved empty list check
            print("There aren't any books in the library.") 
        else:
            print("Here's the list of books in the library:")
            for book in self.books: 
                print(book) 
                
    def search_book(self, author):  # Fix: Corrected search logic
        found_books = [book for book in self.books if book.author == author]
        if found_books:
            print("Here are the search results:")
            for book in found_books:
                print(book)
        else:
            print("No books by this author exist in the library.")

# Simple command-line interface 
def main():
    library = Library() 
    
    while True:
        print("\nLibrary Management System") 
        print("1. Add book") 
        print("2. Borrow book") 
        print("3. Return book") 
        print("4. View books") 
        print("5. Search book") 
        print("6. Exit") 
        
        option = input("Choose an option: ") 
        
        if option == "1": 
            title = input("Enter a book title: ") 
            author = input("Enter author of the book: ") 
            library.add_book(title, author)  # Fix: Updated function call to match corrected method name
            
        elif option == "2": 
            title = input("Enter a book title: ") 
            library.borrow_book(title) 
            
        elif option == "3": 
            title = input("Enter a book title: ") 
            library.return_book(title) 
            
        elif option == "4": 
            library.view_books() 
            
        elif option == "5":
            author = input("Enter a book author: ") 
            library.search_book(author) 
            
        elif option == "6": 
            print("\nExiting Library Management System") 
            break 
        
        else:
            print("Invalid option") 
            
# Running the program 
if __name__ == "__main__": 
    main() 