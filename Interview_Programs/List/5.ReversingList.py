a = [1, 2, 3, 4, 5]

# Initialize an empty list to store reversed element
res = []

# Loop through each item and insert
# it at the beginning of new list
for val in a:
    res.insert(0, val)
print(res)


# Using List Comprehension
a = [1, 2, 3, 4, 5]
rev = [a[i] for i in range(len(a)-1,-1,-1)]
print(rev)