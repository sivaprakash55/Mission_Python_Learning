# To check Nth Fibonacci number

#### Using Recursion

def Fibonacci(n):
    if n <= 0:
        print("Enter correct Input number greater than Zero")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n = int(input("Please enter a Number : "))
print(f"{n}th Fibonacci Number is {Fibonacci(n)}\n")


# creating an array in the function to find the
#nth number in fibonacci series. [0, 1, 1, ...]

print("Second menthod to print series\n")
def fibonacci_series(n):
    if n <= 0:
        exit("Please Enter correct Input number greater than Zero ")
    data = [0, 1]
    if n > 2:
        for i in range(2, n):
            #print(data[i-1],data[i-2])
            data.append(data[i-1] + data[i-2])
    print(data)
    return data

# Driver Program
#n=7
list = fibonacci_series(n)
#print("hi",list,n)
if  n in list:
    print("Given number",n,"is a Fibonacci Series Number in the given range" )

else:
    print("Number",n,"is not a Fibonacci series number in the given range")