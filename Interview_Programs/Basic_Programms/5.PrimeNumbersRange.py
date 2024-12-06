# To get list of Prime numbers from a given range

def prime_numbers(start,stop):
    prime_lst = []
    for num in range(start,stop+1):
        print("entered 1st for",num)
        print("start num is ", start, "stop num is", stop)
        if num > 1:
            print("entered if",num)
            for j in range(2,num):
                print("entered second for",j)
                if (num % j) ==0:
                    print("entered second if",num,j)
                    break
            else:
                print("entered else")
                print(num)


start ,stop = map(int,input("Enter start and stop of range").split(" "))

print("Prime number are ",prime_numbers(start,stop))