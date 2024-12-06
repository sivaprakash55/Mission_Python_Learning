#factorial of number using recursive approach

def factorial(n):
    return 1 if (n==0 or n== 1) else n*factorial(n-1)

n= int(input("Please enter any number : "))
print(f"Factorial of {n} is : {factorial(n)}")