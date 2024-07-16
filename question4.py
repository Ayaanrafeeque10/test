def list_num(lst):  
    concatenated_string =''.join(map(str, lst))
    single_integer = int(concatenated_string)
    return single_integer

list = [11, 33, 50]
result = list_num(list)
print(list)





