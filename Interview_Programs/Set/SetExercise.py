#Add a list of elements to a set
print("Add a list of elements to a set")
sample_set ={"yellow","orange","balck"}
sample_list =["blue","green","red"]
sample_set.update(sample_list)
print(f"\nupdated set is {sample_set}")

#Return a new set of identical items from two sets
print("\nReturn a new set of identical items from two sets")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(f"Intersection of two sets is {set1.intersection(set2)}")

#Get Only unique items from two sets
print("\nGet Only unique items from two sets")
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(f"Union of two sets is {set1.union(set2)}")

#Update the first set with items that don’t exist in the second set
print("\nUpdate the first set with items that don’t exist in the second set")
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(f"difference_update of two sets is {set1}")