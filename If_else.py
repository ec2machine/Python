#match case condition

def choose(today):
    match today:
        case "monday":
            print("today is very good day")
        case "tuesday":
            print("today is nice day")
        case "wensday":
            print("today is wonderfull day")

choose(input("what today:"))