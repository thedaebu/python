## sets
items = {'sword', 'shield'} # set do not have duplicates
items.add('bow')

## turning sets into lists and lists into sets
colors = ['red', 'green', 'red']
set(colors) # => {'red', 'green'} # turns list elements into set data
list(set(colors)) # => ['red', 'green'] # turns set elements into list data

## union and intersection
mine = {'red', 'green', 'blue'}
hers = {'red', 'green', 'black'}

alls = mine | hers # => {'red', 'green', 'blue', 'black'} # combines all
shares = mine & hers # => {'red', 'green'} # only common

## difference and symmetric difference
mine = {'red', 'green', 'blue'}
hers = {'red', 'green', 'black'}

just_me = mine - hers # => {'blue'} # only unique to first item
just_her = hers - mine # => {'black'}
mine.difference(hers)
hers.difference(mine)

symmetric = mine ^ hers # => {'blue', 'black'} # only uncommon
mine.intersection(hers)