# Random Number Generator using PYTHON

# importing random module which allow us to use its functions for random number generation.
import random
def generate_random_number():
    
    print("_________________________ Random Number Generator______________________________________")
    
    print("Rules how to enter a range of number:------------------------")
    print("1. can't enter any one of number as -ve integer and other floating number")
    print("2. can't enter one number as +ve and another as -ve in the same type")
    print("3. can enter any one of number as +ve integer and other floating point")
    
    # Get user input for range
    lower_input = input("Enter a lower number:")
    higher_input = input("Enter a higher number:")
    
    print("\n______________________________________________________________________________________")
    
    # Initialize variables
    lower_input_as_int = None     #  None is a special constant in Python representing the absence of a value or a null value.
    higher_input_as_int = None
    lower_input_as_float = None
    higher_input_as_float = None
    
    try:
        # Try converting str to an integer
        lower_input_as_int = int(lower_input)
        higher_input_as_int = int(higher_input)
    except ValueError:
        try:
            # Try converting str to a float
            lower_input_as_float = float(lower_input)
            higher_input_as_float = float(higher_input)
        except ValueError:
            print("You did not enter a valid number.")
    
    # Check if the range is positive or negative number
    if lower_input_as_int is not None and higher_input_as_int is not None:          # 'is not None' is a way to check if a variable has been assigned a value other than None
        if lower_input_as_int >= 0 and higher_input_as_int > 0:
            # Positive number range
            print(f"Great!!! You entered a Positive integer whose range is {lower_input_as_int} to {higher_input_as_int}")
            random_positive_number = random.randint(lower_input_as_int, higher_input_as_int)
            print("Random positive number:", random_positive_number)

        elif lower_input_as_int < -1 and higher_input_as_int <= -1:
            # Negative number range
            print(f"Great!!! You entered a Negative integer whose range is {lower_input_as_int} to {higher_input_as_int}")
            random_negative_number = random.randint(lower_input_as_int, higher_input_as_int)
            print("Random negative number :", random_negative_number)
        else:
            print("Invalid input. Please enter a valid range.")
    elif lower_input_as_float is not None and higher_input_as_float is not None:
        # Check if the range is positive or negative floating number
        if lower_input_as_float >= 0.1 and higher_input_as_float > 0.1:
            # Positive Floating number range
            print(f"Great!!! You entered a positive floating point number whose range is {lower_input_as_float} to {higher_input_as_float}")
            random_positive_floating_number = random.uniform(lower_input_as_float, higher_input_as_float)
            print("Random Floating positive number:", random_positive_floating_number)

        elif lower_input_as_float < -0.1 and higher_input_as_float <= -0.1:
            # Negative Floating number range
            print(f"Great!!! You entered a Negative floating point number whose range is {lower_input_as_float} to {higher_input_as_float}")
            random_negative_floating_number = random.uniform(lower_input_as_float, higher_input_as_float)
            print("Random Floating negative number :", random_negative_floating_number)
        else:
            print("Invalid input. Please enter a valid range.")
    else:
        print("Invalid input Range.")

# Call the function
generate_random_number()
