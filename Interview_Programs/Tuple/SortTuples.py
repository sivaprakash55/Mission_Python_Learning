tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

tuple2 = tuple(sorted(list(tuple1),key = lambda x:x[0]))
print(tuple2)