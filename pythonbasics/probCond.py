age = int(input("enter age:"))

if age <12:
    print("child")
elif age>14 and age <19:
    print("teenager") 
elif age>=20 and age <40:
    print("young")
elif age>40 and age <60:
    print("oold") 
else:
    print("enter valid")             