text = input("Enter a string: ")
low = []
up = []
ot = []

for i in (text):
    if  i.islower() == True:
        low.append(i)
    elif i.isupper() == True:
        up.append(i)
    else:
        ot.append(i)
uni = set(text)
print("lowercase:", low)
print("uppercase:",up)
print("other:",ot)
print("unique:",uni)

