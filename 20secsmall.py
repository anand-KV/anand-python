#to find second smallest number in the list
a=input("enter the numbers separated with space:")
b=a.split()
s=min(b)
ls=[]
for i in b:
    if(i>s):
     ls.append(i)
     s2=min(ls)
print("second smallest number is:",s2)    
