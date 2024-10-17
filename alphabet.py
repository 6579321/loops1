# Function to check if a character is an alphabet
def is_alphabet(char):
    return (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z')

# Get input from the user
while True:
    user_input = input("Enter a single character: ")

    # Check if the input is a single character
    if len(user_input) == 1:
        if is_alphabet(user_input):
            print(f"'{user_input}' is an alphabet.")
        else:
            print(f"'{user_input}' is not an alphabet.")
        break  # Exit the loop after valid input
    else:
        print("Please enter exactly one character.")
