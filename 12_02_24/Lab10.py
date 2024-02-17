#
#Define a function for calculation sum of two numbers

def sum_of_num(a, b):
     return a+b

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
result = sum_of_num(first_number, second_number)
print(f"Sum of two number is",result)

first_number = str(input("Enter first number: "))
second_number = str(input("Enter second number: "))
result = sum_of_num(first_number, second_number)
print(f"Sum of two number is",result)


