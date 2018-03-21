num=int(input("Enter the value:"))
sum=0
temp = num
while temp>0:
 digit = temp % 10
 sum+= digit **3
 
 if num==sum:
   print("YES")
 else:
    print("NO")
