n=int(input("Enter the number of strings: "))
print("Enter the names")
list=[]
for i in range(0,n):
    x=input()
    list.append(x)
print(list)
count=0
for i in list:
    for j in i:
        if j=='a':
            count=count+1
print("occurence of a=",count)

