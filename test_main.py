from main import subquadratic_multiply, BinaryNumber

## Feel free to add your own tests here.
def test_multiply():
    # Create BinaryNumber instances for the numbers to multiply
    num1 = BinaryNumber(2)
    num2 = BinaryNumber(2)

    # Perform the multiplication using the subquadratic_multiply function
    result = subquadratic_multiply(num1, num2)

    # Assert that the decimal value of the result is as expected
    assert result.decimal_val == 2*2, "Test failed: 2 * 2 should be 4, got " + str(result.decimal_val)

    # If the assertion passes, print a success message
    print("Test passed: 2 * 2 = 4")

# Run the test function
test_multiply()
