def revname(name):
    for word in name[::-1]:
        print (word,end=' ')
n=input("enter your full name:").split()
revname(n)
