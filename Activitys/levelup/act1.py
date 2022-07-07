# Notes
# The int() is a built-in function, this is to convert, or cast, a string to an integer

# While Loop
correct_choice = False
while correct_choice == False:
# Create a program with an input variable that encourages the user to enter a number into the terminal
    user_num = input('Please enter a number... \n')
    try: 
        print(int(user_num), 'is your number' ) # converts the string into an Int data type
        print(type(int(user_num)))# In the terminal it will show Int as the data type
 
        correct_choice = True
    except:
        print(f"Try again, Please enter a number \n")# Try again message
        correct_choice = False
        
        
# Making the program into an function

def user_num():
    answer = input('Please enter a number \n')# Asking the user to enter a number
    
    try:
        print(int(answer)) # converts into the Int data type
        print(type(int(answer))) # In the terminal it will show Int as the data type
    except:
        print('Please try again') # Try again if the users input other than numbers
        user_num()
        
user_num()