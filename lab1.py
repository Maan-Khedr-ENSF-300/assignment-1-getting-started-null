from calculateNums import *
from validateInputs import *

def main():

    user_input = (input(
        "Enter an equation with 3 integer values and 2 operators separated by spaces:\n"))
    input_list = user_input.split(" ")

    numbers_list = getNumbersList(input_list)
    numbers_list = validateNumbers(numbers_list)

    operators_list = getOperatorsList(input_list)
    validateOperators(operators_list)

    answer = performCalculation(operators_list, numbers_list)

    print(f"The answer to {user_input}\n= {answer}")

    displayUserExpression(numbers_list, operators_list.append("="), answer)

if __name__ == "__main__":
    main()
