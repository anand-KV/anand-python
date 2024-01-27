#to write a program to srch an item in a given list and display the number of occurence of the given item
ob=['a','b','b','c','e','c']
print('the list is:',ob)
s=input("Enter item to be searched:\n")
count=0
for i in ob:
    if i==s:
        count+=1
print("number of occurences of",s,':',count)        
