# changing index 

from pandas import *

myseries=Series([10,20,30,40,50])
print(myseries)
myseries.index=['a','b','c','d','e']
print(myseries)
print(myseries[0])
myseries[1]=65   # possible
print(myseries)
