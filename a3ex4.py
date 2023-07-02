row = []
matrix_sum = int
t = []

while True:
    ele = list(input("Enter a row: "))
    if 'x' in ele:
        break
    else:
        for t in ele:
                if t == ' ':
                    ele.remove(t)
        row.append(ele)
        
print(row)
print("\n")
for i in row:
    print(i)
print(type(row))
print("\n")
