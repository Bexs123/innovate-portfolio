# Create a list that represents the alphabet

alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u", "v", "w","x","y","z"]

# Creat a for loop to iterate through this and print each letter in order.

for i in alpha:
    print(i)
    
# Using input, aloow the user to type a number and print the letter it represents in the alphabet.

answer = int(input("Type a number to match the corresponding letter \n" ))
answer -=1
print(alpha[answer])