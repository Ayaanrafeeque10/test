def invert_dict(d):
    inverted_dict = {v: k for k, v in d.items()}
    return inverted_dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
inverted = invert_dict(dict1)
print("Original dictionary:", dict1)
print("Inverted dictionary:", inverted)