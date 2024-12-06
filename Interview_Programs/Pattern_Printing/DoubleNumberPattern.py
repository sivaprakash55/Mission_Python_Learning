#In each column, every number is double it’s the preceding number.

row = 5
for i in range(1,row+1):
    for j in range(i-1,-1,-1):
        # Single asterisk accepts positional parameters only whereas
        # double asterisk accepts keyword parameters
        print(format(2**j,"4d"),end=' ')
    print(" ")