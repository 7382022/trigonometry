# Function to check if the age is valid and even or odd
def check_age():
    try:
        # Get the age from the user
        age = int(input("Enter your age: "))
        
        # Check if the age is valid (positive number)
        if age <= 0:
            print("Error: Age must be a positive number.")
        else:
            # Check if the age is even or odd
            if age % 2 == 0:
                print(f"Your age {age} is Even.")
            else:
                print(f"Your age {age} is Odd.")
    
    except ValueError:
        # Handle the case when the input is not a number
        print("Error: Please enter a valid number for age.")

# Call the function
check_age()
