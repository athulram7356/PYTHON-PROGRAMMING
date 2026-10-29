num= list(map(int,input("Enter numbers:").split()))
print("numbers list:",num)
print("positive numbers:")
for n in num:
    if n>0:
        print(n)

n=int(input("Enter number of elements:"))
num_list=[]

for i in range(n):
    a=int(input("Enter element:"))
    num_list.append(a)
print("Enterd list:",num_list)
sqr_lst=[x**2 for x in num_list]
print("Squred List:",sqr_lst)


word=input("Enter word:")
vowels=[x for x in word.lower()if x in ["a","e","i","o","u"]]
print("vowels:",vowels)


w=input("Enter a word:")
ord=[ord(x) for x in w]
print("ordinal values :",ord)


