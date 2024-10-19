Players = {
    'Rohit': {'runs': 10000, 'centuries': 15},
    'Virat': {'runs': 12000, 'centuries': 18}
}

for key,value in Players.items():
    print(key)
    for key1,value1 in value.items():
        print(f"{key1}:{value1}")
