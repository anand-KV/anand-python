#to write a program to check whether a list is empty or not
li=input("enter comma separated alphabets:")
li=li.split(',')
print(li)
le=len(li)

if(li==['']):
 le=0
print(le) 
if(le>0):
 print("not empty")
else:
 print("empty list:")
