color_list1 = input("enter colors for color_list1 (seperated by spaces):").split()
color_list2 = input("enter colors for color_list2 (seperated by spaces):").split() 
colors_not_in_list2 =[]
for color in color_list1:
    if color not in color_list2:
        colors_not_in_list2.append(color)
print("colors from color_list1 not contained in color_list2",colors_not_in_list2)
