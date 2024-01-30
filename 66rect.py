class rectangle:
    def __init__(self,length=0,breadth=0):
        self.length=length
        self.breadth=breadth
    def __lt__(self,other):
        return self.length*self.breadth<other.length*other.breadth
print("\nrectangle1\n")
a=int(input("enter length:"))
b=int(input("\nenter breadth:"))
print("\nrectangle2\n")
a2=int(input("enter length:"))
b2=int(input("\nenter breadth:"))
r1=rectangle(a,b)
r2=rectangle(a2,b2)
print("\narea of rectangle1 is less than area of rectangle2:\n",r1<r2)
