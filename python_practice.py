## appending to list
healthy = ['kale', 'broccoli', 'blueberry']
healthy.append('oatmeal')

## check if item is in list
# print('kale' in healthy) => True

## removing from list
healthy.remove('oatmeal')

## list comprehenstion
healthy = ['kale', 'broccoli', 'blueberry']
backpack = ['pizza', 'custard', 'crisp', 'kale', 'kale']
backpack[:] = [item for item in backpack if item in healthy]
# first item is the result that is desired
# second item is each item in the backpack list
# third item is includes function

healthy_backpack = []
for item in backpack:
    if item in healthy:
        healthy_backpack.append(item)

squares = []
for i in range(10):
    squares.append(i*i)

squares_list = [i*i for i in range(10)]

## counting items in list
lengths = [len(healthy), len(backpack)] # => [3,5]

## counting specific item in a list
count = backpack.count('kale') # => 2

## sets
backpack2 = {'pizza', 'kale'} # only includes unique items

## counting with list comprehension
counts = [backpack.count(item) for item in backpack]
counts = [[backpack.count(item), item] for item in set(backpack)] # turns backpack list into a set so that each item only is added once

## counting with Counter
from collections import Counter
counts = Counter(backpack) # returns hash of each item and count of each item of a list

## inserting into list
workdays = ['Monday', 'Tuesday', "Thursday", "Friday"]
workdays.insert(2, "Wednesday") # => ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

## removing from list using del
del workdays[2] # => ['Monday', 'Tuesday', "Thursday", "Friday"]
del workdays[-1] # => deletes last item

## removing from list using pop
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
popped = workdays.pop(4) # => 'Friday'

## using del with range
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
del workdays[workdays.index('Wednesday'): workdays.index('Wednesday')+3] # => ['Monday', 'Tuesday']
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
del workdays[workdays.index('Thursday')] # => ['Monday', 'Tuesday', 'Wednesday']

## removing from list using while loop
backpack = ['pizza', 'custard', 'crisp', 'kale', 'kale']
while 'kale' in backpack:
    backpack.remove('kale')

## removing from list using for loop
backpack = ['pizza', 'custard', 'crisp', 'kale', 'kale']
for item in backpack[:]:
    if item == 'kale':
        backpack.remove('kale')

## removing from list using list comprehension
backpack = ['pizza', 'custard', 'crisp', 'kale', 'kale']
backpack = [item for item in backpack if item != 'kale'] # => ['pizza', 'custard', 'crisp']

## reversing a list
data = [0,1,2,3,4,5]
data.reverse() # => [5,4,3,2,1,0]

## swapping items in a list
data = [0,1,2,3,4,5]
data[0], data[1] = data[1], data[0] # => [1,0,2,3,4,5]

## reversed iterator
reversed(data) # does not return anything but can be used in a for loop

## reversing list with slice
data = [0,1,2,3,4,5]
data[:] = data[::-1] # => [5,4,3,2,1,0]

## sorting a list
workdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
sorted(workdays) # sorts list without changing the original list
workdays.sort() # sorts list by modifying the original list

## sorting a list of numbers in reverse order
data = [1,6,8,3,9,2,5]
sorted(data, reverse=True) # put in reverse parameter for sorted

## sorting a list of strings regardless of capitalization
strings = ['a', 'Abc', 'A', 'abc', 'aBc']
strings.sort() # sorts by capital letter first
strings = ['a', 'Abc', 'A', 'abc', 'aBc']
strings.sort(key=str.lower) # sorts first by letter and then by key

## sorting a list of strings by length
strings = ['a', 'Abc', 'A', 'abc', 'aBc']
sorted(strings, key=len) # sorted way
strings.sort(key=len) # .sort way

## sorting a list of numbers lexicographically
numbers = [1,-1,3,-23,-34,2]
numbers.sort(key=str) # => [-1,-23,-34,1,2,3] sorts according to first digit by negative then positive

## sorting a list of different data types numerically
stuff = [True, False, 0, -1, '0', '10', 5, '9001']
stuff.sort(key=float)

## converting a string into a list
msg = 'hello world'
words = msg.split(' ') # => ['hello', 'world']
msg = '''hello
world''' # use three quotes to be able to use line breaks for a string
words = msg.split('\n') # => ['hello', 'world']

## getting user input
# print('Sup nerd')
# response = input()

## concatenating items in a list
data = ['this', 'is', 'data']
' '.join(data) # => 'this is data'
data = ['this', 'is', 'data', 5, 10]
' '.join(str(i) for i in data) # parameter is a list data type so list comprehension can be used

## sorting 2D lists
data = [[5,8,2,9], [92], [56,1,82]]
sorted(data) # sorts by first item of each nested list
data = [['ball', 'apple'], ['amazon'], ['a', 'zen']]
sorted(data) # if previous items are the same, starts sorting by subsequent items

## sorting lists by key
def avg(nums):
    return sum(nums) / len(nums)

data = [[10,2,3], [10,4,4], [4,2,3], [10,1,1]]
data = sorted(data, key=avg) # function can be used as key as long as argument data type matches list item data type
