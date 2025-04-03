class Book:
    def __init__(self, title, author): 
        self.title = title 
        self.author = author 
        self.is_borrowed = False
        
    def __str__(self):
        self.status = self.is_borrowed #checking the availability of a book 
        if self.status is self.is_borrowed:
            return "Book is available." 
        else:
            return "Book is currently borrowed." 
        
class Library: 
    def __init__(self): 
        self.books = [] #list of books in the library 
            
    def add_books(self, title, author): #adding books to the library
        self.books.append(Book(title, author)) 
        print("The book", title, "by", author, "has been added to the library.") 
            
    def borrow_book(self, title): #checking whether a book has been borrowed or not 
        self.title = title
        for book in self.books: 
            if book.title is not book.is_borrowed: 
                book.is_borrowed = True 
                print("The book", title, "is currently borrowed.")
            else: 
                print("The book", title, "is available.") 
                    
    def return_book(self, title): #checking whether a book has been returned or not 
        for book in self.books: 
            if book.title == book.is_borrowed: 
                print("The book", title, "is currently borrowed.") 
            elif book.title is False: 
                print("The book", book.title, "has not been returned.") 
            else: 
                print("The book", book.title, "has been returned.") 
    
    def view_books(self): #displaying all the books as well as their statuses 
        if self.books == [] : 
            print("There aren't any books in the library.") 
        else:
            for book in self.books: 
                print("Here's the list of books in the library: ", book) 
                
    def search_book(self, author): #searches for a book by its title 
        for author in self.books: 
            if author in self.books: 
                print("Here are the search results:\n ",Book) 
            else:
                print("The book does not exist in the library.")

#simple command line interface 
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
            library.add_books(title, author) 
            
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
            print("\n Exiting Library Management System") 
            break 
        
        else:
            print("Invalid option") 
            
#running the program 
if __name__ == "__main__": 
    main()