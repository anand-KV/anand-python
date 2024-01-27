num=input("enter numbers separated by commas:")
lst=num.split(",")
ev=[n for n in lst if n%2==0]
print("even numbers are:",ev)
