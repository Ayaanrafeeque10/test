collection1 = [1, 2, 3, 4, 5]
collection2 = [4, 5, 6, 7, 8]
set1 = set(collection1)
set2 = set(collection2)
common_entites = set1.intersection(set2)
common_entites_list = list(common_entites)
print("common numbers", common_entites_list)