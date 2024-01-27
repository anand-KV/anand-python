#to accept a sentence frm usr and display the total count of vowels in the sentence
s=input("enter the sentence:\n")
count=0
for i in s:
    if i.lower()=='a'or i.lower()=='e'or i.lower()=="i"or i.lower()=="o"or i.lower=="u":
        count+=1
print("number of vowels:",count)        
