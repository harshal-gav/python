
dict_x = {'key1': 1, 'key2': 3, 'key3': 2}
dict_y = {'key1': 1, 'key2': 2}

for key in dict_x:
    if key in dict_y and dict_x[key] == dict_y[key]:
        print("is present in both x and y")
