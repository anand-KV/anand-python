#file handling
#to remove specific lines from a file
try:
    fr=open("file1.txt",'r')
    re=fr.readlines()
    fw=open("file02.txt",'w+')
    for i in re:
       if i.strip("\n")!="7.seven":
        fw.write(i)
        print("remove successfully")
except Exception as e:
    print(e)
finally:
    fr.close()
    fw.close()
