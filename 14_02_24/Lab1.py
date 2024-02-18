def say_hello():#non return type and no parameter
   print("Hello")

say_hello()


def say_hello_arg(name):  # non return type and with argument
    print("Hello", name)


say_hello_arg("pramod")


def say_hello_arg(name, age):  # non return type and with  more argument
    print("Hello", name, age)


say_hello_arg("pramod", 67)



def say_hello_arg_default(name ="pramod"):  # non return type and with default value
    print("Hello", name)


say_hello_arg_default()
