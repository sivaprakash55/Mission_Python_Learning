tuple1 = (10, 20, 30, 40, 50)
print(f"Reverse of the given tuple is {tuple1[::-1]}")

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(f"accessing only values 20 is {tuple1[1][1]}")

print("Unpacking Tuple")
tuple1 = (10, 20, 30, 40)
a,b,c,d = tuple1
print(f"First Values is {a} \nSecond Value is {b} \nThird Value is {c} \nFourth Value is {d}")