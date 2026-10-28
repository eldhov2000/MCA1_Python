s=float(input("Enter the side of the square: "))

a=int(input("Enter the digit:"))

b=int(input("Enter the second digit:"))

c=float(input("Enter the base of triangle:"))

d=float(input("Enter the height of the triangle:"))

sqarea= lambda side: side*side
print("Area of Square:",sqarea(s))

recta=lambda length,width: length * width
print("Area of Rectangle:",recta(a,b))

tria= lambda base,height: 0.5* base* height
print("area of Triangle:",tria(c,d))