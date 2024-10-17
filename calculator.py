# Function to calculate power using a loop
def calculate_power(base, exponent):
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    # If exponent is negative, return the reciprocal
    return 1 / result if exponent < 0 else result

# Get input from the user
while True:
    try:
        base = float(input("Enter the base number: "))
        exponent = int(input("Enter the exponent (n): "))
        result = calculate_power(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}.")
        break  # Exit the loop after valid input
    except ValueError:
        print("Please enter valid numbers.")
