num = input("Enter number to guess: ")
num2 = 0

while num != num2:
    num2 = input("Enter number: ").lower()
    
    if num < num2:
        print("Your number is bigger")
        
    elif num > num2:
        print("Your number is smaller")
    
    if num2 == 'exit':
        print("You lost!")
        #break
        num = 'exit'
        
if num == num2 and num != 'exit':
    print("Congratulations!")
