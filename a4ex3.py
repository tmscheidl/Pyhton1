def create_train_test_splits(data: list, train_size: float) -> tuple:
    results = []
    datas = []
    split_1 = data[:int(len(data)*train_size)]
    split_2 = [x for x in data if x not in split_1]
    
    results.append(split_1)
    results.append(split_2)
    
    datas.append(data)
    datas.append(train_size)
    
    data = tuple(datas)
    result = tuple(results)
    
    return print("create_train_test_splits"+str(data)+" = ", result)

create_train_test_splits([], 0.5)
create_train_test_splits(list(range(10)), 0.5)
create_train_test_splits(list(range(10)), 0.67)
