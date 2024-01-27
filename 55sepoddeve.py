#program to separate odd and even number in a file for separate files
fr=open("num1.txt",'r')
ls=fr.readlines()
ls.pop()
print(ls)
even=[x for x in ls if not int(x)%2]
odd=[x for x in ls if not int(x)%2]
fw1=open("eve.txt",'w+')
evenlst=[x+"\n" for x in even ]
fw1.writelines(evenlst)
fw2=open("odd.txt",'w+')
oddlst=[x+"\n" for x in odd ]
fw2.writelines(oddlst)
