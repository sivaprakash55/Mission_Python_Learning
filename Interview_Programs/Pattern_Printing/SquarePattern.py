rows = 5

for i in range(1,rows+1):
    for j in range(1,rows+1):
        print(i if j <= i else j ,end=" ")
    print(" ")

