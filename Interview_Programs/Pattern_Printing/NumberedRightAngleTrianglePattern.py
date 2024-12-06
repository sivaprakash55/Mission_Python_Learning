print("Pyramid Pattern Increment")
for i in range(1,6):
    for j in range(i):
        print(i , end=" ")
    print("")
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
print("Inverted Pyramid Pattern Decrement reverse order")
for i in range(5,0,-1):
    for j in range(i):
        print(i ,end =" ")
    print("")

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

print("Inverted Pyramid Pattern   same order")
cntr =0
for i in range(5,0,-1):
    cntr += 1
    for j in range(i):
        print(cntr , end =' ')
    print(" ")

1 1 1 1 1
2 2 2 2
3 3 3
4 4
5  