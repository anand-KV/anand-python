def sumdig(n):
    if not (n/10):
        return n
    else:
        return(n%10)+sumdig(n//10)
y=int(input("Enter a digit:"))    
print(sumdig(y))
