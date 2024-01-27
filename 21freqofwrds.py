#program to determine frequency of words in a sentence
s=input("enter a sentence:")
wrd={}
for x in s.split():
    wrd[x]=wrd.get(x,0)+1
print("number of words:",wrdn)    
