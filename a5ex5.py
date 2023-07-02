print("Welcome to Data Statistics!")
print("\n")
print("Available actions:")

print("a - Add number:")
print("v - View the calculated statistics: ")
print("x - Exit the program: ")
print("\n")


s = 0
mi = None
ma = 0
count = 0
x = None

while True:
    a = input("Enter action: ")
        
    if a != 'a' and a != 'v' and a != 'x':
        print("Invalid action. ", a, " Try again")
    
    if a == 'a':
        while a == 'a':
            
            x = input("Enter number or 'x' when you are done: ")

            if x == 'x':
                break
            else:
                count += 1
                s = s + int(x)
                avg = s / count
        
                if int(ma) < int(x):
                    ma = x
            
                if mi is None or int(mi) > int(x):
                    mi = x
            
    if a == 'v':
        if x != None and count != 0 :    
            print("Count: ", count)
            print("Sum: ", s)
            print("Avg: ", avg)
            print("Min: ", mi)
            print("Max: ", ma)
        else:
            print("No numbers have been added yet!")
    
    if a == 'x':
        print("Bye!")
        break
