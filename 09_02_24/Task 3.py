# GENERATE FIBONACCI SERIES

n = int(input("Enter the number till you want to generate Fibonacci Series: "))
a=0
b=1
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c, end=" ")