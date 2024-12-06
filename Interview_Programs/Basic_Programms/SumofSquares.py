# To get sum of squares of first N natural numbers
def sumOfSquares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + pow(i,3)
    return sum

n = int(input("Please enter a Positive non-zeor number: "))
print(f"Sum of squares upto given number is {sumOfSquares(n)}")