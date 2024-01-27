def sum(seq):
    if len(seq)==1:
        return (seq[0])
    else:
        return (seq[0]+sum(seq[1:]))
n=input("Enter space separated elements:")
n=list(map(int,n.split( )))
print(sum(n))
