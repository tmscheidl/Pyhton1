def gen_range(start: int, stop: int, step: int = 1):
    empty = list()
    result = list()
    
    if step == 0:
        print("ValueError")
        return
    elif isinstance(start,int) and isinstance(stop,int) and isinstance(step,int):
        if step < 0:
            if stop <= start:
               # print(start)
                result.append(start)
                print(result)
                result += empty
                gen_range(start + step, stop, step)
            else:
                return print(result)
        else:
            if start <= stop:
               # print(start)
                result.append(start)
                print(result)
                result += empty
                gen_range(start + step, stop, step)
            else:
                return print(result)
    else:
        print("TypeError")
        return

    
        
gen_range(-10,-3,2)
