#to accept percentage of marks from user and display the grade
a=int(input("Enter the percentage of marks:"))
if(a>=90):
  print("A+=>NICE")
elif(a>=80 and a<90):
  print("A=>VERY GOOD")
elif(a>=70 and a<80):
  print("B+=>GOOD")
elif(a>=60 and a<70):
  print("B=>AVERAGE")
elif(a>=50 and a<60):
  print("C+=>NOT BAD")
elif(a>=40 and a<50):
  print("C=>PASS")
else:
  print("F=>FAIL")  
