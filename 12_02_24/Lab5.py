#Match Case
#switch

num = int(input("Enter a number from 1 to 6: "))
match num: #breaek is not needed
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _:
        print("No idea what you entered")