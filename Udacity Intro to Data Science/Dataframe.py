from numpy import *
from pandas import *
d = {'name': Series(['Braund', 'Cummings', 'Heinkken', 'Allen'], index=['a', 'b', 'c', 'd']),
     'age': Series([22, 38, 26, 35], index=['a', 'b', 'c', 'd']),
     'fare': Series([7.25, 71.83, 8.25], index=['a', 'b', 'd']),
     'survived': Series([False, True, True, False], index=['a', 'b', 'c', 'd'])}
df = DataFrame(d)
print df
