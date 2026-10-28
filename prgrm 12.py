n=int(input("Enter the number of colours:"))
color_list=[]
for i in range(n):
    color=input("Enter the color:")
    color_list.append(color)
print(color_list)
print("The first color is:",color_list[0])
print("The first color is:",color_list[-1])

