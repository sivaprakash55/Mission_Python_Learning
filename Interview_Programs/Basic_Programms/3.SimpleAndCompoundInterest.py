#Simple interest of given amount is SI = (P*t*r)100

def Simple_interest(p,t,r):
    si = (p*t*r)/100
    return si

p = int(input("Please enter Principle amount : "))
t = int(input("Please enter tenure in years : "))
r = int(input("Please enter rate of interest : "))
print(f"Simple Interest of given amount is {Simple_interest(p,t,r)}")


#Compound Interest of given amount is CI = P(1+R/100)*t

def Compound_interest(p,t,r):
    ci = p * (pow((1+r/100),t))
    return ci

p = int(input("Please enter Principle amount : "))
t = int(input("Please enter tenure in years : "))
r = float(input("Please enter rate of interest : "))
print(f"Compound Interest of given amount is {Compound_interest(p,t,r)}")