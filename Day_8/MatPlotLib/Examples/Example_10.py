# pie chart

""" Autopct — The autopct parameter specifies the format of the text that will be displayed inside the pie slices. It allows you to customize how the percentage of each slice is shown. """

from matplotlib import pyplot as py

fruits=['Apple','Mango','Banana','Water_melon']
quantity=[30,50,15,5]

# inside "autopct" 0.1  means 1 decimal point

py.pie(quantity,labels=fruits,autopct='%0.1f%%',colors=['red','blue','yellow','pink'])
#py.pie(quantity,labels=fruits,colors=['red','blue','yellow','pink'])
py.legend()
#py.legend(bbox_to_anchor=(0.9,0.9))
#py.legend(bbox_to_anchor=(1.3,0.1))
py.show()