def eve(l):
    for i in l:
        if(i==237):
            break
        elif not i%2:
            print(i)
n=input("enter collection of integers:")
n=list(map(int,n.split()))
eve(n)
