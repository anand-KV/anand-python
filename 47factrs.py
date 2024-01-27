#to write a program to generate all factors of a given numbers
def factors(n):
    for i in range(1,n):
        if not n%i:
            print(i,end='')
n=int(input("Enter number:\n"))
print("The factors of",n,"are:\t",end='')
factors(n)
