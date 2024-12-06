# To check given number is prime or not
# Negitive numbers and 0,1 are not prime

num = int(input("Enter the desired number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
    if flag:
        print ("The number entered is not a prime number")
    else:
        print ("The number entered is a prime number")

###############

num = 11
if num > 1:
    for i in range(2,(num//2)+1):
        print("iteration number",i)
        if (num % i) ==0:
            print("number is not prime ")
            break
    else:
            print(" prime number")
else:
    print("Please enter a number bigger than 1")

