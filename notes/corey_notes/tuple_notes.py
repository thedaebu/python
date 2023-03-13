# import namedtuple
from collections import namedtuple

# first argument is name of tuple type
# second argument is list of attribute names in order
dndStats = namedtuple('dndStats', ['str', 'armor', 'dex', 'cha'])

player1 = dndStats(4,4,7,8)
# # value can be retrieved using attribute name
# print(player1.armor)
# # value can be retrieved using index
# print(player1[0])