#program to find no of lines in a file
try:
    fr=open("file1.txt",'r')
    ls=fr.readlines()
    print("no of lines in a file is:",len(ls))
except Exception as e:
    print(e)
finally:
    fr.close()
