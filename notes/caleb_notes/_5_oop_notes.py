## object-oriented programming
class Book():
    # class variable
    # using class name for prefix refers to class
    # using self for prefix refers to class instance
    favorites = []

    # all instance methods require first argument of self  
    def __init__(self, title, pages): # initializer/constructor method
        self.title = title
        self.pages = pages

    def is_long(self):
        if self.pages > 100:
            return True
        else:
            return False

    # decorator for class method
    # cls must be used as first argument to represent the class
    @classmethod
    def add_to_favorites(cls, book):
        cls.favorites.append(book)

    # class method can be used for alternate constructor method
    @classmethod
    def from_string(cls, book_str):
        title, pages = book_str.split("-")
        return cls(title, pages)

    # denotes method as static method
    @staticmethod
    def is_long(pages):
        return pages > 100

    # accessor decorator allows defining through a method but can also be 
    # accessed as an attribute
    @property
    def book_code(self):
        return f'{self.title}-{self.pages}'

    # setter decorator for property method
    # use method_name.setter as decorator name
    # use same method name for method name
    @book_code.setter
    def book_code(self, code):
        title, pages = code.split("-")
        self.title = title
        self.pages = pages

    @book_code.deleter
    def book_code(self):
        self.title = None
        self.pages = None

    # defines/overwrites return of class instantiation
    def __repr__(self):
        return f'{self.title} is {self.pages} long'

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
        return hash(self.title) ^ hash(self.pages)

# subclass has superclass as initial argument
class ShortStory(Book):
    def __init__(self, title, pages, genre):
        super().__init__(title, pages)
        self.genre = genre

# use one leading underscore when naming class variables
# use __slots__ to set an array of class variables to be used for Python to work faster
# inheritance
	# use more general class as argument for more specific class
	# in __init__ method, use the super().__init__ method
# getter method
	# use @property on the line before the getter method
# setter method
	# use @variableName.setter before the setter method
book1 = ShortStory("The Book", 12, "Horror")

# returns if instance is instance of a class/superclass
print(isinstance(book1, Book))
print(isinstance(book1, ShortStory))
# returns if class is subclass of a superclass
print(issubclass(ShortStory, Book))

# delete method call for class
del book1.book_code
