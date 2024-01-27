#to generate a list of four digit numbers in a given range with all their digit even
#and the number is a perfect square
def digi_even(num):
    flag=0
    while num>0:
        d=num%10
        if d%2:
            flag=1
            break
        num=num//10
        if flag==1:return False
        else:return True
def perfect_squ(num):
    flag=0
    for i in range(num//2+1):
        if i*i==num:
            flag=1
            break
    if flag==1:return True
    else:return False
lower=int(input("Enter lower limit:\n"))
upper=int(input("Enter upper limit:\n"))
print("numbers between",lower,'and',upper,'is',end=" ")
for i in range(lower,upper+1):
    if digi_even(i)and perfect_squ(i):
        print(i,end='')
        
