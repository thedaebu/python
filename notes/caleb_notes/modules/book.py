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
        return hash(self.title) ^ hash(self.pages)

    # defines/overwrites to make list of object invoke __str__
    def __repr__(self):
        return self.__str__()