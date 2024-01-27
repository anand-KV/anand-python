#accept a string and return the length of longest word if the result has more than one word ,then print('bingo')
a=input("enter a sentence:\n")
a=a.split()
b=[len(x)for x in a]
b=max(b)
leng=[x for x in a if (len(x)==b)]
if(len(leng)>1):
    print('BINGO')
