def remove_duplicates(collection):
    unique_elements = []
    for element in collection:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

collection = [1, 2, 3, 1, 2, 4, 5, 3]
unique_collection = remove_duplicates(collection)
print("Original collection:", collection)
print("Collection without duplicates:", unique_collection)
