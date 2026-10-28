s=str(input("Enter the Line Of Text :"))
count= dict()
words = s.split()
for x in words:
    if x not in count:
        count[x]=1
    else:
        count[x]+=1
print(count)