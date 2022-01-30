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

## exceptions
try:
    file = open('asdasd.txt', 'r')
except Exception as e: # where error occurs, following runs
    e # type of exception
    print('Cannot find file')
finally: # 'finally' will always run after block is run
    file.close()

## with
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