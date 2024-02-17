# Generate the factors of the number


num = int(input("Enter the number for the Factor: "))
if num < 0:
    print("Factorial of the number is not possible")
elif num == 0:
    print("Factorial of the number is 1")
else:
    n=1
    for i in range(1,num+1):
        n = n* i
print("Factorial of ", num, "is" ,n )