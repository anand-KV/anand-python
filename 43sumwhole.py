def whole(x):
    if not x:
        return 0
    else:
        return x+whole(x-1)
y=int(input("enter a number:"))
print(whole(y))
