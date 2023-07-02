def clip(*values, min_=0, max_=1) -> list:
    
    lst = []
    value = list(values)
    for i in range(len(value)):
        if value[i] < min_:
            lst.append(min_)
           # min_1 = value[i]
        elif value[i] > max_:
            lst.append(max_)
           # max_1 = value[i]
        else:
            lst.append(value[i])
                   
    if min_ == 0 and max_ ==1:
        return print("clip"+str(values)+" =", lst)
    elif min_ == 0:
        value.append(max_)
        values = tuple(value)
        return print("clip"+str(values)+" max_="+str(max_)+" =", lst)
    elif max_ == 1:
        value.append(min_)
        values = tuple(value)
        return print("clip"+str(values)+" min_="+str(min_)+" =", lst)
    else:
        value.append(max_)
        value.append(min_)
        values = tuple(value)
        return print("clip"+str(values)+" min_="+str(min_)+" max_="+str(max_)+" =", lst)

clip()
clip(1, 2, 0.1, 0)
clip(-1, 0.5)
clip(-1, 0.5, min_=-2)
clip(-1, 0.5, max_=0.3)
clip(-1, 0.5, min_=2, max_=3)
