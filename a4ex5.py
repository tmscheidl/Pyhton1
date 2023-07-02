def sort(elements: list, ascending: bool = True):
    lst = []
    min = elements[0]
    max = elements[0]
    
    if ascending == True:
        for i in range(len(elements)):
            for j in range(i+1, len(elements)):
                if elements[i] > elements[j]:
                    elements[i], elements[j] = elements[j], elements[i]
    else:
        for i in range(len(elements)):
            for j in range(i+1, len(elements)):
                if elements[i] < elements[j]:
                    elements[i], elements[j] = elements[j], elements[i]
    return print("sort(elements, "+str(ascending)+") -> some_list =",elements)

some_list = [1, 3, 0, 4, 5]                
sort(some_list)   
sort(some_list, False)                
