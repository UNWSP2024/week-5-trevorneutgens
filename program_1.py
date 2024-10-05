# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    """Convert kilometers to miles using the conversion factor."""
    miles = kilometers * 0.621371
    return miles  # Return the converted miles

def test_kilometer_conversion():
    """Run tests to validate the kilometer_conversion function."""
    # Test the conversion of 5 kilometers
    result = kilometer_conversion(5)
    assert abs(result - 3.106855) < 1e-5  # Allow for small floating-point precision issues

    # Additional test cases
    assert abs(kilometer_conversion(0) - 0.0) < 1e-5  # 0 km should be 0 miles
    assert abs(kilometer_conversion(10) - 6.21371) < 1e-5  # 10 km should be about 6.21371 miles

if __name__ == '__main__':
    # Run tests first
    test_kilometer_conversion()
    print("All tests passed!")

    # Get User Input
    print('Kilometer to Miles Converter')

    while True:
        try:
            kilometers = float(input("Enter distance in kilometers: "))
            if kilometers < 0:
                print("Please enter a non-negative number.")
                continue  # Prompt again if the input is negative
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle invalid inputs

    # Call kilometer_conversion
    miles = kilometer_conversion(kilometers)

    # Display the miles with 5 decimal precision
    print(f'Your distance in miles is: {miles:.5f} miles')