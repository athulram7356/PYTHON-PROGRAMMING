c=int (input("Enter the Current Year:"))
f=int(input("Enter the Final Year:"))
print("the future Leap Years are:")
for x in range(c,f+1):
    if (x%4==0 and x%100!=0) or (x%400==0):
        print(x)