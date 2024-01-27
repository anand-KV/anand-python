#to enter 2 collection of integers;chck
#->whether they are of same length
#->whether they sum to same value
#->whether any value occur in both
s1=input("enter the first set of numbers:\n")
s1=set(map(int,s1.split(',')))
s2=input("enter the second set of numbers:\n")
s2=set(map(int,s2.split(',')))
print("is both sets are of same length:",len(s1)==len(s2))
print("is sum of both sets are equal:",sum(s1)==sum(s2))
print("both set has atleast one common value:",bool(s1.intersection(s2)))
