#to create a single string separated with space from 2 strings by swapping the characters at position1.
x1=input("enter the first string:")
x2=input("enter the second string:")
a=x1[0]
b=x2[0]
x1=b+x1[1:]
x2=a+x2[1:]
print("Final string:",x1,x2)
