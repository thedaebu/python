## string data type
	# len()
	# [range]
	# .index()
	# .count()
	# .format()
		- numbers in brackets correspond to arguments for .format
		- first = 'my'
		- second = 'dude'
		print('Hello {0} {1}.'.format(first, second))
## boolean operators
	# not
	# and
	# or
## comparison operators
	- same as Ruby ==
## equality operators
	# is / is not - preferable
	# == / !=
## if statements 
	# ex. 
		if a is true:
			print(a)
		elif b is true:
			print(b)
		else:
			print(c)
## while statements
	# ex.
		spam = 0;
		while spam < 5:
			spam += 1
	# break
	 	- used to break the while loop if a certain condition is met
	# continue
		- used to restart the loop when a certain condition is met
## pass
	- must be used in place of the absence of code
	# ex. 
		if True:
			pass
## None
	- the value used to signify the absence of a value
## functions
	- order arguments in the same order as parameters
	- do not specify in the arguments for parameters without default values
	- do specify in the arguments for parameters with default values
	- arguments can be specified by using the specified parameter variable name
	# ex.
		def printThis(name, copyright = 'copyright'):
			print(name + copyright)
		printThis('DB', copyright = '2021')
	# lambda function (anonymous functions)
		# ex. add = lambda (a,b): a + b
## join
	- join is used on the separator and the array is the argument
	# ex. print(','.join(array_of_strings))
## format
	- based on arguments	
		- used in place of interpolating
		# ex. 'Hello {0} {1}.'.format('my', 'dude') => 'Hello my dude.'
	- for commas for numbers
		# ex. '{:,}'.join(12345) => '12,345'
## input
	- used for retrieving input from user
	- save the input to a variable
	- the argument for input is a string for the user
	# ex. answer = input('how are you?')
## built-in data types
	## list
		- lists are like arrays
		# x = []
		# x = list() - preferable
		# list comprehension
			# x = [i for i in sentence if is_consonant(i)]
	## tuple
		- tuples are immutable lists
		- tuples are made without using any enclosures
		# numbers = (1,2,3)
		# numbers = 1,2,3
	## range
		# range(full range)
		# range(start, end)
		# range(start, end, increment)
		- range is non-inclusive
	## dictionaries
		- dictionaries are like hashes
		# a = {'a': 1, 'b': 2, 'c': 3}
		# a = dict(a=1, b=2, c=3)
	## sets
		- set are hashes without values
		- used to removed duplicates
		- used to test if an object is included
		- used for mathematical operators
		# new_set = {'new', 'set'}
		# letters = set('hello') => {'h', 'e', 'l', 'o'}
## built-in functions
	## filter(function, iterable)
		- creates a new iterable of the same type which includes each item for which function 		  returns true
	## map(function, iterable)
		- creates a new iterable of the same type which includes the result of calling the function 		on every item in the iterable
		# ex. sqs = map(lambda x: x**2, range(2))
			list(sqs)
	## sorted(iterable, key=None, reverse=False)
		- creates a new sorted list from the items in the iterable
	## enumerate(iterable, start=0)
		- starts with a sequence and converts it into a series of tuples
		- each tuple is made up of an index and value
	## zip(*iterables)
		- creates a zip object filled with tuples that combine 1-to-1 the items in each provided 		iterable
## function arguments
	## *args
		- used for arguments not part of a variable
	## **kwargs
		- keyword arguments
		- arguments used as key-value pairs
## importing in Python
	- module is Python code in a separate file
	- package is the path to a directory that contains modules
	- __ini__.py is the default package for a package
	- submodule is a file in a module's folder
	# import statements
		# import <module>
		# import <package>.<subpackage>.<module>
		# from <package> import <module>, <module>
		# from <package> import <function>
		# from <package> import <module> as <altName>
## classes
	- each method needs self as the first argument
	- use one leading underscore when naming class variables
	- use __slots__ to set an array of class variables to be used for Python to work faster
	- use __repr__ to make return of class instance prettier
	- inheritance
		- use more general class as argument for more specific class
		- in __init__ method, use the super().__init__ method
	- getter method
		- use @property on the line before the getter method
	- setter method
		- use @<variable_name>.setter before the setter method
	# ex. class Employee:
		__slots__ = ['_id']

		def __init__(self, id):
			self._id = id

		@property
		def id(self):
			return self._id
	
		@id.setter
		def id(self, value):
			if value > 0
				value = 0
			self._id = value
			return self._id
		
		def __repr__(self):
			return f'<Employee ({self._id})>'

	          class Manager(Employee):
		def __init__(self, id):
			super().__init__(id)
			self.empoyees = []
		}