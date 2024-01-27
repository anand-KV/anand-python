a=input("Enter the words separated with commas:")
b=int(input("enter a number:"))
c=a.split(',')
l=[]
for i in range (len(c)):
    if(b<len(c[i])):
     l.append(c[i])
     print(l)
