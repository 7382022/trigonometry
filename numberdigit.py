# Get the number from the user
number = input("Enter a number: ")

# Check if the input is a valid number
if number.isdigit() or (number[0] == '-' and number[1:].isdigit()):
    # Count the number of digits
    print(f"The total number of digits is {len(number.lstrip('-'))}.")
else:
    print("Error: Please enter a valid number.")
