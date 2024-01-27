#to find largest of 2 numbers using lambda func
largest=lambda x,y:x if x>y else y
x=int(input("enter the 1st number:"))
y=int(input("enter the 2nd number:"))
print(largest(x,y))
