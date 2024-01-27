yr1=int(input("enter the current year"))
yr2=int(input("enter the future year"))
le=[i for i in range(yr1,yr2)if i%4==0]
print("leap years from",yr1,"to",yr2,"is:",le)
