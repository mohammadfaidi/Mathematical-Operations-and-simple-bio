


print("Menu options:")
print("1-Mathematical operations")
print("2-Simple bio operations")
print("\n")
option1 = int(input(":"))

def sumation(no1,no2):
    sum = no1 + no2
    print("sumation :" + str(sum))

def multpication(no1,no2):
    sum = no1 * no2
    print("multpication :" + str(sum))

def substration(no1,no2):
    sum = no1 - no2
    print("substration:" + str(sum))

def divison(no1,no2):
    sum = no1 / no2
    print("divison:" + str(sum))


def bio(name, city, family):
    print("name:" + name)
    print("city:" + city)
    print("family members :" + family)


if option1 < 1 or option1 >2:
    print("Out of the range ")


elif option1 == 1:
    no1=int(input("Enter your first number:"))
    no2=int(input("Enter your second number:"))
    operator=input("Select type of operator + or - or * or /:")

    if operator == '+':
        sumation(no1,no2)
    elif operator == '-':
        substration(no1,no2)
    elif operator == '*':
        multpication(no1,no2)
    elif operator =='/':
        divison(no1,no2)
    else:
        print("your operator is not include")


elif option1 == 2:
    name=input("Enter your first and second name:")
    city=input("Enter your city:")
    family=input("Enter your familty member:")
    bio(name,city,family)



