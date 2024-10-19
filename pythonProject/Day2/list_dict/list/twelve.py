li=["Black", "Red", "Maroon", "Yellow"]
li1=["#000000", "#FF0000", "#800000", "#FFFF00"]
li2=[{'color_name':color,'color_code':code} for color,code in zip(li,li1) ]
print(li2)