a=[]
n=int(input("Enter number of value:"))
for i in range(1,n+1):
    c=int(input("Enter element:"))
    a.append(c)
a.sort()
print("Largest element is:",a[n-1])
