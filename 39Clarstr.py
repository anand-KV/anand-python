lar_string=lambda s:[x for x in s.split() if len(x)>5]
a=input("enter collection of strings")
print(lar_string(a))
