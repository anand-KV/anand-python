v=['a','e','i','o','u','A','E','I','O','U']
a=input("Enter a string:")
x=list(a)
vo=[n for n in x if(n in v)]
print("Vowels in the given string:",vo)
