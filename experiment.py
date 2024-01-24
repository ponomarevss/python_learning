new_dict = {'a': 1, 'b': 8, 'c': 4}
sorted_dict = sorted(new_dict.items(), key=lambda x: x[1], reverse=True)
print(new_dict, sorted_dict)
