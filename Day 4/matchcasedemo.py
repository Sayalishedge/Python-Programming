color="Red"
match color:
    case "Red":
        print("you selected red")
        print("this is another line in RED")
    case "yellow":
        print("you selected yellow")
        print("this is another line in yellow")
    case _:
        print("you selected default case")
        print("this is another line in RED")

color="Red"
match color:
    case "Red":
        print("you selected red")
        print("this is another line in RED")
    case "yellow":
        print("you selected yellow")
        print("this is another line in yellow")
    case Otherwise:
        print("you selected default case")
        print("this is another line in RED")


num=3
match num:
    case 1|3|4:
        print("you are in 1|2|3 case")
    case 5:
        print("you are in 5 case")
    case _:
        print("you are in default case")

        
