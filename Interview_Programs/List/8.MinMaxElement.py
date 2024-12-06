# Using loop

lst = [12,23,546,9990,43234]
min,max = lst[0],lst[0]
for i in lst:
    if max < i:
        max = i
    elif min > i:
        min = i
print("min element is",min,"Max element is", max)

# Using sort()
lst.sort()
print("min element is",lst[0],"Max element is",lst[-1])


def even_odd_list(list):
    even_lst=[]
    odd_lst =[]
    for i in list:
        if i %2 ==0:
            even_lst.append(i)
        else:
            odd_lst.append(i)
    return even_lst,odd_lst

print(f"list of even and odd numbers is {even_odd_list(lst)}")

