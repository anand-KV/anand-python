#genrating  STR by combining first 2 char and last two char from an input str
#if the length of input string is 2,then result str must be a concatenation of these
#char or if length is less than 2,return an empty thing
s=input("enter a string:")
if len(s)==2:
   new=s*2
elif len(s)==2:
    new=''
else:
    new=s[:2]+s[-2:]
print("new string:",new)    
