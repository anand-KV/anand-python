s=input("enter the string:")
chr=s[0]
s=s.replace(chr,"&")
s=chr+s[1:]
print("Final string is:",s)
