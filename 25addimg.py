#to write a python program to add 'img' at the end of the string.if alredy ends with 'img',then add'ly'
a=input("enter a string:\n")
if (a.lower().endswith ('ing')):
    a=a+'ly'
else:
    a=a+'ing'
print(a)    
    
