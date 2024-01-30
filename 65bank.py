class bank:
    def __init__(self,number=0,name="empty",acctype="empty",balance=0):
        self.number=number
        self.name=name
        self.acctype=acctype
        self.balance=balance
    def deposit(self,balance=0):
         self.balance=self.balance+balance
    def withdraw(self,balance=0):
        if not self.balance:
            print("zero balance")
        else:
            balance= int(input("enter the amount to withdraw:"))
            if(self.balance-balance)<0:
                print("insufficient balance")
            else:
             self.balance=self.balance-balance
    def showdetails(self):
        print("\n----account deatils---\n")
        print("holder name:",self.name)
        print("acc number:",self.number)
        print("acc type:",self.acctype)
        print("acc balance",self.balance)
nam=input("enter your name:")
num=input("\nenter your accnumber:")
typ=input("\nenter your acctype:")
x=bank(nam,num,typ)
x.showdetails()
while(1):
    print("\n1.deposit\n2.withdraw\n3.details\n4.exit")
    y=int(input("\nenter your choice:"))
    if(y==1):
        n=int(input("enter the amnt to deposit:"))
        x.deposit(n)
    elif(y==2):
        
        x.withdraw()
    elif(y==3):
        x.showdetails()
    else:
        print("exit")
        break
    
           
    
