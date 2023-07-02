age = int(input("Enter age: "))
if age <= 0:
    print("Error, Invalid age")
elif age<= 7:
    print("Child Ticket: 10$")
elif age <= 17:
    print("Teenager Ticket: 15$")
elif age >= 18:
    sal= int(input("Enter salary: "))
    if sal <= 0:
        print ("Error, Invalid salary")
        quit()
    elif sal <= 1000:
        print("Reduced Adult ticket 1: 20$")
    elif sal <= 2000:
        print("Reduced Adult ticket 2: 25$")
    else:
        print("Adult ticket: 30$")     


