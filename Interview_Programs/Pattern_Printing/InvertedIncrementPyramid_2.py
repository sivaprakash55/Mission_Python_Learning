print("Inverted Increment Pyramid Pattern ")
rows = 5
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print("")


1
2 1
3 2 1
4 3 2 1
5 4 3 2 1