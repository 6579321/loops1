# Function to swap three numbers
def swap_numbers(a, b, c):
    return c, a, b

# Get input from the user
while True:
    try:
        # Input three numbers
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))

        # Swap the numbers
        a, b, c = swap_numbers(a, b, c)

        # Display the result
        print(f"After swapping: First number = {a}, Second number = {b}, Third number = {c}.")
        break  # Exit the loop after valid input
    except ValueError:
        print("Please enter valid numbers.")
