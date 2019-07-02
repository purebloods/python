x1= (int) (input("Enter x1:"))
y1= (int) (input("Enter y1:"))
x2= (int) (input("Enter x2:"))
y2= (int) (input("Enter y2:"))
x3= (int) (input("Enter x3:"))
y3= (int) (input("Enter y3:"))

a=(((x1-x2)/(y1-y2))-((x3-x1)/(y3-y1)))
if(a==0):
     print ("yes")
else:
     print ("No")
