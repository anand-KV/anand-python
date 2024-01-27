#to accept a list of char and convert it into a string
x=input("enter a list of characters:")
x=x.split()
s=' '
for i in x:
    s=s+i
print("string=",s)    
