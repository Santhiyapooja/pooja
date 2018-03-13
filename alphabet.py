print("Enter '0' for exit.");
str = input("Enter any character: ");
if str == '0':
    exit();
else:
    if((str>='a' and str<='z') or (str>='A' and str<='Z')):
    	print(str, "is an alphabet.");
    else:
    	print(str, "is not an alphabet.")
