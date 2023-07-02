start = int(input("start: "))
stop = int(input("stop: "))
step = int(input ("step: "))

print("\n")
odd_counter = 0
even_sum = 0

for i in range(start,stop,step):
    
    x = len(range(start,stop,step))

    if i % 2 == 1:
        odd_counter += 1
    elif i % 2 == 0:
        even_sum = even_sum + i
        
    if i == start + step :
        print("2nd value in range = ", i)
    if i == start + (x-1) * step :
        print("Last value in range = ", i)
print("odd_counter = ", odd_counter)
print("even_sum = ", even_sum)



