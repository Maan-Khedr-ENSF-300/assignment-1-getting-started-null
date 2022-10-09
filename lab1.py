from calculateNums import *
from validateInputs import *
from tests import *

def main():
    unit_test_flag = True
    integration_test_flag = True

    if unit_test_flag == True:
        unitTests()
    if integration_test_flag == True:
        integrationTests()

    # receives user input and creates list from it
    user_input = (input(
        "Enter an equation with 3 integer values and 2 operators separated by spaces:\n"))
    input_list = user_input.split(" ")

    # creates a valid list of integers from user input
    numbers_list = getNumbersList(input_list)
    numbers_list = validateNumbers(numbers_list)

    # creates a valid list of operators from user input
    operators_list = getOperatorsList(input_list)
    validateOperators(operators_list)

    # Calculates the answer to the math expression and stores it as a variable
    answer = performCalculation(operators_list, numbers_list)

    # append "=" to end of operators list to meet requirements and calls the display function
    operators_list.append("=")
    displayUserExpression(numbers_list, operators_list, answer)

if __name__ == "__main__":
    main()
