# Using loop
lst = [2,4,8,3]
res = 1
for i in lst:
    res *= i
print("Multiplication of list using list is :",res)

# Using reduce()
from functools import reduce
from operator import mul
res = reduce(mul,lst)
print("Multiplication of list using list is :",res )

# Using math.prod()
