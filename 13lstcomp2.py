lst=[]
a=int(input("enter the size of the list:"))
print("enter",a,"numbers:")
for i in range(0,a):
  b=int(input())
  lst.append(b)
print(lst)
print("square of numbers")
ps=[n*n for n in lst if n>=0]
print(ps)  
