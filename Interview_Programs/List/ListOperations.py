l1 =[10,20,30,40,50]
l2 =[60,70,80,60]

print(10 in l1) # True
print(90 not in l2) #True
print(l1+l2) #[10, 20, 30, 40, 50, 60, 70, 80, 60]
print(l1*2)  #[10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
print(l1[3]) #40
print(l1[1:4]) #[20,30,40]
print(l2[0:3:2]) #[60,80]
print(len(l2)) #4
print(l2.count((60))) #2
print(l1.index(30)) # 2
print(l1.index(40,1,4)) # 3
print(min(l1)) #10
print(max(l2)) #80
print(l1.append(100),l1) #[10, 20, 30, 40, 50, 100]
print(l2.append([1,2,3]),l2) #[60, 70, 80, 60, [1, 2, 3]]
l2[2]=100
print(l2) #[60, 70, 100, 60, [1, 2, 3]]
l2.remove(60) #removes 1st occurence of item
print(l2) #[70, 100, 60, [1, 2, 3]]
l1.pop(0)
print(l1) #[20, 30, 40, 50, 100]
print(l1.clear()) #None clears the list
l3 = l2.copy()
print(l3) #[70, 100, 60, [1, 2, 3]]
