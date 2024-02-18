
def reverse_string(str):
    rev_str = ""
    for i in str:
        rev_str = i + rev_str
    return rev_str

name = input("Enter your name which you want to reverse: ")
reversed_name = reverse_string(name)
print("Reversed name is ",reversed_name)


