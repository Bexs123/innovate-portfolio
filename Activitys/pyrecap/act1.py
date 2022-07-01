#Create variable that holds the text "welcome to Code Nation"
string_1 = "welcome to Code Nation"
print(string_1)

#Find the length of the string and save this to a new variable
string2_len = len(string_1)
print(string2_len)

#Create a function that checks if the string length is even
def odd_even_checker(string_1):
    string2_len = len(string_1)
    if string2_len%2==0:
# If it is even print the length of the string and an appropriate message
        print(f"The length of the string {string_1} is {string2_len} and yes it even")
    else:
# Do the same but with a different message if it is odd
        print(f"The length of the string {string_1} is {string2_len} it is odd")
    
#Change the string length so you can test all possible outcomes
odd_even_checker("welcome 2 Code Nation")
odd_even_checker("welcomes too Code Nationss")
odd_even_checker("welcome too Code Nation")
odd_even_checker("welcom t Code Ntion")
odd_even_checker("welcome to Code Nationss")
odd_even_checker("welcome to Code Nationssee")