book_set ={"python","java","scala","golang"}
#insertion order is not maintained as original set
for item in book_set:
    print(item)

#check if item is present in set
print("checking element present in Set")
if "java" in book_set:
    print("element present")
else:
    print("no")

#adding new items to set
print("Adding new items to set")
book_set = {'Harry Potter', 'Angels and Demons'}
print(f"original set is {book_set}")
book_set.add("python")
print(f"new Set after adding item with add() {book_set}")
# {'python', 'Harry Potter', 'Angels and Demons'}
book_set.update(['scala','rust'])
print(f"new Set after adding item with update() {book_set}")
#{'python', 'rust', 'Harry Potter', 'Angels and Demons', 'scala'}


##Removing set items
print("Removing set elements")
color_set = {'red', 'orange', 'yellow', 'white', 'black'}
print(f"Original set is {color_set}")
color_set.remove('yellow')
print(f"set after removing element with remove('yellow') is {color_set}")
color_set.discard("blue")
print(f"discard doesn't give error and set is {color_set}")
new_set = color_set.pop()
print(f"new set after pop() is {color_set}")
color_set.clear()
print(f"set after using clear() is {color_set}")
del new_set

#Set Operations
print("********* Set Operations *******")
color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}

res = color_set.union(remaining_colors)
print(f"Union of both Sets are {res}")

res = remaining_colors.intersection(color_set)
print(f"Intersection of both sets is {res}")
print("original set is ",color_set)

print(f"intersection_update of both sets")
remaining_colors.intersection_update(color_set)
print("original set is ",remaining_colors)


color_set.difference(remaining_colors)
print(f"Difference of both sets is {color_set}")

print(f"difference_update of both sets")
remaining_colors.difference_update(color_set)
print("original set is ",remaining_colors)

res = remaining_colors.symmetric_difference(color_set)
print(f"symmetric difference of both sets is {res}")