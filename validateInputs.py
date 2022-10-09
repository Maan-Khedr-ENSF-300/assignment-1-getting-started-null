# receives a list of the full equation and parses it into a list of the numerical values
def getNumbersList(equation_list: list) -> list:
    return [(equation_list)[i] for i in range(len(equation_list)) if i % 2 == 0]

# receives a list of the full equation and parses it into a list of the operators
def getOperatorsList(equation_list: list) -> list:
    return [(equation_list)[i] for i in range(len(equation_list)) if i % 2 != 0]

# receives a list of numerical string values and attempts to return it as a list of integers. Function will be called recursively until valid input is received.
def validateNumbers(numbers_list: list) -> list:
    try:
        integer_list = [int(x) for x in numbers_list]
        return integer_list
    # Created exception handling for inputs that are not integer values
    except Exception as e:
        if "invalid literal for int() with base 10" in str(e):
            valid_input_list = input(
                "One or more of your numbers is invalid, enter an equation with 3 integer values and 2 operators separated by spaces:\n").split(" ")
            valid_numbers_list = getNumbersList(valid_input_list)
            validateNumbers(valid_numbers_list)
        else:
            raise e

# receives a list of operator string values and will call the function recursively until all operators are valid
def validateOperators(operators_list: list) -> None:
    valid_operators = ['+', '-', '*', '/']

    invalid_inputs = [x for x in operators_list if not (x in valid_operators)]

    # This function will be called recursively until there are no invalid inputs
    if len(invalid_inputs) != 0:
        valid_input_list = input(
            "One or more of your operators is invalid, enter an equation with 3 integer values and 2 operators separated by spaces:\n").split(" ")
        valid_operators_list = getOperatorsList(valid_input_list)
        validateOperators(valid_operators_list)

def displayUserExpression(list_of_numbers, list_of_operators, final_answer):
    final_output = ""
    for i in range(len(list_of_numbers)):
        final_output += f"{list_of_numbers[i]} {list_of_operators[i]} "

    final_output += f"\n{final_answer}"
    print(final_answer)
