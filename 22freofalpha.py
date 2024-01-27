#program to determine frequency of alphabets in a word
a=input("enter a word:")
li={}
for x in a:
    li[x]=li.get(x,0)+1
print("number of letters:",li)    
    
