## object-oriented programming
class Book():
    # class variable
    favorites = [] 

    # all class method require first argument of self    
    def __init__(self, title, pages): # initializer/constructor method
        self.title = title
        self.pages = pages

    # class method
    def is_long(self):
        if self.pages > 100:
            return True
        else:
            return False

    # defines/overwrites str representation of an object in a class
    def __str__(self):
        return f"{self.title} is {self.pages} pages long."

    # defines/overwrites equal comparison between same class objects
    def __eq__(self, other):
        if (self.title == other.title and self.pages == other.pages):
            return True
        else:
            return False

    # defines/overwrites class object to be hashable for use in dictionaries/sets
    def __hash__(self):
        return hash(self.title)  ^ hash(self.pages)

book1 = Book('Second Wind', 102) # book object
book2 = Book('Second Wind', 102) # book object

Book.favorites.extend([book1, book2])
Book.favorites[0].title # => 'Second Wind'
Book.favorites[0] # => 'Second Wind is 102 pages long.'
book1 == book2 # => True # must use '==' and not 'is'
hash(book1) == hash(book2) # => True

def change_title(book): # passed by object reference method
    book.title = "Third Wind"

change_title(book1) # book1.title changes to "Third Wind"

## reading and writing to a file
open('input.txt', 'a') # first argument is name, second argument file command
open('input.txt', 'a') # 'a' is append mode
file = open('input.txt', 'w') # 'w' is write mode
file.write('Second Wind\t102\n')
file.write('Third Wind\t102')
file.close() # closes access to file

file = open('input.txt', 'r') # 'r' is read mode
data = file.read() # assigns content of file to variable
file.close()

# exceptions
try:
    file = open('asdasd.txt', 'r')
except Exception as e: # where error occurs, following runs
    e # type of exception
    print('Cannot find file')
finally: # 'finally' will always run after block is run
    file.close()

# with
with open('input.txt') as file: # 'with' runs file.close() after everything in with block is run
    if not file.closed:
        print('open')

try:
    file = open('input.txt')
except:
    print('Something is wrong')
else: # 'else' runs if no exceptions come up
    with file:
        print(file.readline())