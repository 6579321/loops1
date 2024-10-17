# Function to get ASCII value of a character
def get_ascii_value(char):
    return ord(char)

# Get input from the user
while True:
    user_input = input("Enter a single character: ")

    # Check if the input is a single character
    if len(user_input) == 1:
        ascii_value = get_ascii_value(user_input)
        print(f"The ASCII value of '{user_input}' is {ascii_value}.")
        break  # Exit the loop after valid input
    else:
        print("Please enter exactly one character.")
