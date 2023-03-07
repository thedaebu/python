## generator
# does not hold values in memory
# is faster because it waits to be used
def square_it(nums):
    for i in nums:
        yield i*i
        # yield command makes it a generator

my_nums = square_it([1,2,3,4])
print(next(my_nums))
print(next(my_nums))

my_nums = (i**i for i in [1,2,3,4])
# generator can be created using list comprehension between parentheses

list(my_nums)
# generator can be turned into a list
