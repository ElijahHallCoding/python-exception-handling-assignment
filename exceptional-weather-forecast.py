# Task 1

def get_temperature():
    # Ask user for temperature input with exceptions handling
    try:
        # User enter temperature in fahrenheit
        temp_fahrenheit = float(input("Please enter the temperature in fahrenheit: "))
        print(f"the temperature you entered is {temp_fahrenheit}F.")
    except ValueError:
        # Print if user does not enter valid number
        print("You did not enter a valid number. Please try again.")
    except Exception as e:
        # Handle unforseen exceptions
        print(f"An unexpected error occurred: {e}")

# Call the function
get_temperature() 

def convert_to_celsius(fahrenheit):
    # Conversion (Fahrenheit - 32) * 5/9
    celsius = (fahrenheit - 32) * 5/9
    # Return Celsius
    return celsius

# Task 2: Temperature Conversion

# Get temperature from user and convert
def convert_temperature():
    try:
        # User input for temp in Fahrenheit
        temp_fahrenheit = float(input("Please enter the temperature in fahrenheit: "))
        # Convert entered temp to celsius
        temp_celsius = convert_to_celsius(temp_fahrenheit)
        # Display temp conversion
        print(f"The temperature in Celsius is {temp_celsius:.2f}C.")
    except ValueError:
        # Handle invalid user input
        print("That was not a valid number. Please enter a numerical value.")
    except Exception as e:
        # Handle any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

# Call the function
convert_temperature() 

# Task 3: User Experience

def convert_to_celsius(fahrenheit):
    # Conversion formula
    celsius = (fahrenheit - 32) * 5 /  9
    # Return the temp
    return celsius

# User input
def convert_temperature():
    try: 
        # User input in Fahrenheit
        temp_fahrenheit = float(input("Please enter the temperature in Fahrenheit: ")) 
        # Convert the temp the celsius
        temp_celsius = convert_to_celsius(temp_fahrenheit)
    except ValueError:
        # Handle user input error
        print("That was not valid. Please enter a numerical value.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    else:
        # Display converted temp for user
        print(f"{temp_fahrenheit} degrees Fahrenheit is {temp_celsius:.2f} degrees celsius.")

# Call the function to run the temp conversion
convert_temperature()

# Task 4: finally

def convert_to_celsius(fahrenheit):
    # Conversion formula
    celsius = (fahrenheit - 32) * 5 /  9
    # Return the temp
    return celsius

 #User input
def convert_temperature():
    try: 
        # User input in Fahrenheit
        temp_fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
        # Convert the temp the celsius
        temp_celsius = convert_to_celsius(temp_fahrenheit)
    except ValueError:
        # Handle user input error
        print("That was not valid. Please enter a numerical value.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
    else:
        # Display converted temp for user
        print(f"{temp_fahrenheit} degrees Fahrenheit is {temp_celsius:.2f} degrees celsius.")
    finally:
        # Thank the user
        print("Thank you for using the weather forecast application!")

convert_temperature() 



