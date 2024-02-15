# Create a list called 'color_list' containing color names
color_list = ["Red", "Green", "White", "Black"]


# Function to test printing the first and last elements of the color_list
def test_print_first_last_elements():
    # Capture the output of the print statement using a StringIO object
    from io import StringIO
    import sys
    output = StringIO()
    sys.stdout = output

    # Perform the action to be tested
    print("%s %s" % (color_list[0], color_list[-1]))

    # Get the printed output
    printed_output = output.getvalue().strip()

    # Assert statements to check the printed output
    assert printed_output == "Red Black"
    assert printed_output != "Red White"  # This assertion will fail

    # Reset sys.stdout to the default
    sys.stdout = sys.__stdout__

def test_print_first_last_elements1():
    # Capture the output of the print statement using a StringIO object
    from io import StringIO
    import sys
    output = StringIO()
    sys.stdout = output

    # Perform the action to be tested
    print("%s %s" % (color_list[1], color_list[-1]))

    # Get the printed output
    printed_output = output.getvalue().strip()

    # Assert statements to check the printed output
    assert printed_output == "Red Black"
    assert printed_output != "Red White"  # This assertion will fail

    # Reset sys.stdout to the default
    sys.stdout = sys.__stdout__

# Run the test function
test_print_first_last_elements()
