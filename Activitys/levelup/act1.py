correct_choice = False
while correct_choice == False:
    user_num = input("Please enter a number...")
    try:
        print(int(user_num), "is you number" )
        print(type(int(user_num)))
        correct_choice = True
    except:
        print(f"please enter a number, try again...")
        correct_choice = False