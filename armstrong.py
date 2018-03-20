lower=int(input("Enter the lower:"))
upper=int(input("Enter the upper:"))
 
for num in range(lower,upper + 1):
   # initialize sum
   sum = 0
 
   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
 
   if num == sum:
       print(num)
