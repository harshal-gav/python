# violinplot
import statistics
from matplotlib import pyplot as py

first=[1,2,3,4,5,6,7,8,9]
second=[1,2,3,4,5,4,3,2,1]
third=[6,7,8,9,8,7,6,5,4]

data=list([first,second,third])
py.violinplot(data,showmedians=True,quantiles=[[0.25,0.5,0.75],[0.25,0.5,0.75],[0.25,0.5,0.75]])
#py.violinplot(data)
#print(py.violinplot.__doc__)
print(statistics.mean(first))
print(statistics.mean(second))
print(statistics.mean(third))
py.show()