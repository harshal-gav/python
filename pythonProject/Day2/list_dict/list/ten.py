def check(lst, n):
    if n < len(lst):
        return f"The {n}-th element exists and it is: {lst[n]}"
    else:
        return f"The {n}-th element does not exist in the list."


my_list = [10, 20, 30, 40, 50]
n = 3
print(check(my_list, n))

