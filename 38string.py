def count_string(s):
    count=0
    for i in s.split():
        if len(i)>1 and i[0]==i[-1]:
            count+=1
    return count
s=input("enter a collection of string:")
print(count_string(s))
