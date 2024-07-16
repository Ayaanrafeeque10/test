def common_min_dict(dict1, dict2):
    common_keys = set(dict1.keys()) & set(dict2.keys())
    result_dict = {}
    
    for key in common_keys:
        result_dict[key] = min(dict1[key], dict2[key])
    
    return result_dict

dict1 = { 'a': 5, 'b': 10, 'c': 15 }
dict2 = { 'a': 3, 'b': 12, 'd': 20 }

common_min = common_min_dict(dict1, dict2)
print("Common minimum dictionary:", common_min)