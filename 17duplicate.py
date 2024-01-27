a=input("Enter the numbers separated with commas:")
b=a.split(',')
print(b)
ls=[]
for i in b:
 if(i not in ls):
    ls.append(i)
print(ls)  
