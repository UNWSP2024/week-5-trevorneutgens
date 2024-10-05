# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    # Convert kilometers to miles using the conversion factor
    miles = kilometers * 0.621371
    return miles  # Return the converted miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp
#### conversion logic in the temp_conversion function
if __name__ == '__main__':
    # Get User Input
    print('Kilometer to Miles Converter')

    while True:
        try:
            kilometers = float(input("Enter distance in kilometers: "))
            if kilometers < 0:
                print("Please enter a non-negative number.")
                continue
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Call kilometer_conversion
    miles = kilometer_conversion(kilometers)

    # Display the miles
    print(f'Your distance in miles is: {miles:.5f} miles')