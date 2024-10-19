def fun(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                return True
    return False

l1=[1,2,3,4,5]
l2=[6,3,8,9,0]
print(fun(l1,l2))