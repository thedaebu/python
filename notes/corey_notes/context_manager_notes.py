## context managers help with overall work related to files
with open('some_file.txt', 'w') as file:
    # file.write()
    pass

# creating a context manager using a class
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename,
        self.mode = mode

    # the with statement runs the code within the enter method
    # the alias is a reference to the return of the enter method
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with Open_File('sample.txt', 'w') as f:
    f.write('Testing')

# creating a context manager using a method/generator
# import contextmanager
from contextlib import contextmanager

# use contextmanager decorator
@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        # everything above yield is equivalent to enter method
        yield f
    finally:
        # everything below yield is equivalent to exit method
        f.close()

with open_file('sample.txt', 'w'):
    f.write('hello')

# context manager for changing directories
# import os
import os

# use contextmanager decorator
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)
