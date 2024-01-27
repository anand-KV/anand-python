#to accept a list of integers frm user for all values abve 100 store the str 'over' in the specific position
n=list(map(int,input("Enter numbers:\n").split()))
count=1
for i in n:
    if i>100:
       n[count]='over'
       count+=1
print(n)        
