def binary_search(elements: list, x) -> bool:

    low = 0
    high = len(elements) - 1
    mid = 0
    if isinstance(x,int):
        if high == low:
            if elements[mid] == x:
                return True
            else:
                return False
        else:
            if high > low:
                mid = (low + high) // 2
                if elements[mid] == x:
                    return True
                elif elements[mid] > x:
                    element = elements[:len(elements)//2]
                    return binary_search(element,x)
                else:
                    element = elements[len(elements)//2:]
                    return binary_search(element,x)
            else:
                return False
    else:
        return False


my_sorted_list = [1, 2, 5, 7, 8, 10, 20, 30, 41, 100]
binary_search(my_sorted_list, 8)
