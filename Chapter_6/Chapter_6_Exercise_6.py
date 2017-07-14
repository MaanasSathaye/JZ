#Use Heron's formula to calculate the area of a triangle (with inputs of three sides). This works with negative numbers
#as well to accommodate for unit circle work.

import math

x = abs(float(input("What is the length of the first side of your triangle? ")))
y = abs(float(input("What is the length of the second side of your triangle? ")))
z = abs(float(input("What is the length of the third side of your triangle? ")))

def heron(x,y,z):
    perimeter = x + y + z
    area = math.sqrt((perimeter-x)*(perimeter-y)*(perimeter-z))
    print(area)

print ("The area of your triangle is", heron(x,y,z))
