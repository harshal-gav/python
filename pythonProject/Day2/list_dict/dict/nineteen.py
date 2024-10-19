
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

merged_dict = dic1.copy()

merged_dict.update(dic2)
merged_dict.update(dic3)


print(merged_dict)
