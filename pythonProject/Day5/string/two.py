def modify_string(s):
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'


sample1 = 'abc'
sample2 = 'string'


print(modify_string(sample1))
print(modify_string(sample2))
