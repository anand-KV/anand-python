#to create a list of first names ,count the number of nmaes that starts with "a".
a=input("enter nmaes separated by commas:")
name=list(s.split(","))
name=[item.split('')for item in names]
count=0
print("first names:")
l=(item[0]for item in  name)
print(l)
for item in names:
    print(item[0])
    if[item[0][0]=='a'or item[0][0]=='A']:
        count=count+1
print("names that starts with A is",count)        
