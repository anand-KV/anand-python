def rev(s):
    if not len(s):
        return ' '
    else:
        return s[-1]+rev(s[:-1])
st=input("enter a string:")
print(rev(st))
