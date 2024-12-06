#Creating Dict

person = {"name":"siva","country":"india","sex":"male","age":30}
print(person)

# create a dictionary using dict()
person1 = dict({"name":"anu","country":"india","sex":"female","age":29})
print(person1)

# create a dictionary from sequence having each item as a pair
person2 = dict([("name","saanvi"),("country","india"),("sex","female"),("age",1)])
print(person2)

# create dictionary with value as a list
person3 = {"name": "Jessa", "telephones": [1178, 2563, 4569]}
print(person,"\n")

#accessing Dict values
print("accessing elements using dict['key']")
print("person name is ",person["name"],"\n")

print("accessing elements using get()")
print(f"person country is {person1.get("country")}\n")

#Get all keys and values
person = {"name" :"jessica","country":"USA","telephone":"17896"}

#get all keys
print("Get all keys using dict.keys()")
print(f"Keys of person dict are {person.keys()}\n")

#get all values
print("Get all values using dict.values()")
print(f"Values of person dict are {person.values()}\n")

#get all key
print("Get all Items using dict.items()")
print(f"Items of person dict are {person.items()}\n")

#Iterating a dictionary
person = {"name": "Jessa", "country": "USA", "telephone": 1178}
print(f"keys :")
for key in person:
    print(f"key : {person.keys()}")

print(f"\nvalues : ")
for value in person:
    print(f"value : {person.values()}")

print("\n")
##Adding items to the dictionary
print("adding new key-value with direct assignment : person['weight']=70 \noriginal dict is",person)
person["weight"]=70
print("new dict is",person,"\n")

print("adding new key-val with update() : person.update({'height':160}) \noriginal dict is",person)
person.update({"height":160})
print("new dict is",person,"\n")

#set defaults
print("set defaults for a dict \noriginal dict is ",person)
person.setdefault('state','Andhra')
print("new dict is :",person)

# if value not mentioned for new key default is None
print("if value not mentioned for new key default is None")
person.setdefault('GovtJob')
print("new dict is : ",person)

#if we want to update exsting key it won't update old values
print("if we want to update exsting key it won't update old values")
person.setdefault('state','TS')
print("new dict is :",person)

#Modify the values of the dictionary keys
print("\nModify the values of the dictionary keys")
person["country"] = 'India'
print(f"updated dict with person['country'] = 'India' is \n{person}\n")

person.update({"country": "SriLanka"})
print(f"updated dict with person.update() is \n{person}\n")