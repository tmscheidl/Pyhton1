def flatten(nested: list) -> list:
    flat = []

    for i in nested:
        if isinstance(i,list):
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat

flatten([1, 2, [4, [8, 9, [11, 12], 10], 5], 3, [6, 7]])
#flatten([[]])
#flatten([[], [], [1], [], [1, [], [4, 5, [[[6]]]], 2, 3]])
