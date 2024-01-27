#to write lambda func,each to find area of square ,rectangle and triangle
import math
#square
a=int(input("Enter side of square:\n"))
area=lambda a:a*a
print("Area of the square:",area(a))
#rectangle
a,b=int(input("Enter length:\n")),int(input("Enter breadth:\n"))
area=lambda a,b:a*b
print("Area of the rectangle:",area(a,b))
#triangle
a=list(map(int,input("enter length of 3 sides of triangle").split()))
s=(a[0]+a[1]+a[2])/2
area=lambda a,s:math.sqrt(s*(s-a[0])*(s-a[1])*(s-a[2]))
print("Area of the triangle:",area(a,s))
