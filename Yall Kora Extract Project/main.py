import datetime
from yalla_kora import yallaKora
print("===================")
print("Welcome To you :)")
print("===================")

while True: 
    print("What do you want: ")
    print("-----------------")
    print("1- show today's matches")
    print("2- show matches in onther day")
    print("3- Exit ")
    choice = int(input("Enter your choice: "))
    if choice == 1: 
        x = datetime.datetime.now()
        day = x.day
        month = x.month
        year = x.year
        date = f"{month}/{day}/{year}"
        matchs = yallaKora(date)
        matchs.show_mathces()
    elif choice == 2: 
        day = input("Enter the day number (1 to 31): ") 
        month = input("Enter the month number (1 to 12): ") 
        year = input("Enter the year : ") 
        date = f"{month}/{day}/{year}"
        matchs = yallaKora(date)
        matchs.show_mathces()
    elif choice == 3: 
        break; 
    else : 
        print("Enter a number between 1 to 3 !")


print("Thank you for using our app")