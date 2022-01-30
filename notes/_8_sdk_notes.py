## SDK
# references modules/book.py and sdk/booksSDK.py
import modules.book as Book
import sdk.booksSDK as booksSDK
book = Book.Book('Ciao', 21)
# booksSDK.add_book(book)
books = booksSDK.get_books()
returnedBook = booksSDK.get_book_by_title('Cia')

# creating a console app
def print_menu():
    print("""Choose an option:
    1. print all books
    2. add a book
    3. update a book
    4. delete a book""")

while True:
    print_menu()
    response = int(input())
    if response == 1:
        for book in booksSDK.get_books():
            print(book)
    elif response == 2:
        print('What is the name of the book?')
        title = input()
        print ('How many pages are in the book?')
        pages = int(input())
        book = Book.Book(title, pages)
        booksSDK.add_book(book)
    elif response == 3:
        print('Which book would you want to update?')
        title = input()
        if not book:
            print("Sorry, that book does not exist")
        else:
            print('What is the new title of the book?')
            new_title = input()
            print('How many pages does the new book have?')
            new_pages = str(input())
            print(booksSDK.update_book(title, new_title, new_pages))
    elif response == 4:
        print('Which book do you want to delete?')
        title = input()
        print(booksSDK.delete_book(title))
    else:
        print('Thank you')
        break