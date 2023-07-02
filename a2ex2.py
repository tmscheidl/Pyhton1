text = str(input("Enter text: "))
count = 0
for a in text:
    if (a.isupper()) == True:
        print("The uppercase letter: ", a)
        count += 1
print("The input text contains ", count, " uppercase characters.")
