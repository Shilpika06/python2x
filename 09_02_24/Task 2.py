"""Enter three inputs sides for the triangle
 and determine if the triangle is isosceles or equilateral or scalene"""

side1=int(input("Enter the first side: " ))
side2=int(input("Enter the second side: "))
side3=int(input("Enter the third side: "))
if side1 == side2 and side2 == side3  or side1 == side3 :
 print("Triangle is equilateral")
elif side1== side2 or side2==side3:
  print("Triangle is isosceles")
else:
  print("Triangle is scalane")
