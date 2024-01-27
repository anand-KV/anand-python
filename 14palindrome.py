#to accept a string and check whether it is plaindrome
s=input("enter a string:")
re=s[::-1]
print(re)
if(s==re):
   print("string is plaindrome:")
else:
   print("string is not a palindrome:")
