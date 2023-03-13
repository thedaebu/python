# does not hold values in memory
# is faster because it waits to be used
def square_it(nums):
    for i in nums:
        # yield command makes return a generator
        yield i*i

my_nums = square_it([1,2,3,4])
print(next(my_nums))
print(next(my_nums))

# generator can be created using list comprehension between parentheses
my_nums = (i**i for i in [1,2,3,4])

# generator can be turned into a list
list(my_nums)
