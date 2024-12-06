#To check given number is Armstrong or not
# Sum of cubes of each digit is equal to original number
# 153 = 1*1*1 + 5*5*5 + 3*3*3 = 1+125+27 = 153

n = int(input("Please enter any Integer : "))
temp = n # stroing original num in temp variable
#l = len(str(n)) #get len of digit
sum = 0

while n != 0 :
    rev = n % 10
    print("rev :",rev)
    sum = sum + pow(rev,3)
    print("sum :",sum)
    n = n // 10
    print("n :",n)

if temp == sum:
    print("temp :",temp)
    print("sum ",sum)
    print(f"Entered number is Armstrong")
else:
    print(f"Entered number is Not Armstrong")