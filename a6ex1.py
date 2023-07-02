import re
def read_numbers(path: str) -> list: 
    f = open(path,"r")
    a = []
    b = []
    
    for i in f:
        s = [s for s in re.findall(r'-?\d+\.?\d*', i)]
        
        for j in s:
                a.append(j)
                x = ", ".join(a)
    b.append(x)
        
    return b

read_numbers("ex1_data.txt")
