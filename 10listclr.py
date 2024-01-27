#to create a list of colors from comma separated list of color names entered by user;print alternate colors

b=input("enter the colours:")
c=b.split(',')
print(c)
print(c[::2])
