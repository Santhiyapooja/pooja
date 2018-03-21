num=int(input("Enter upper range:"))
num1=int(input("Enter lower range:"))
my_list=[]
for x in range(num+1,num1):
    my_list.append(x)
odd_list=list(filter(lambda x:(x%2!=0),my_list))
print(*odd_list)
