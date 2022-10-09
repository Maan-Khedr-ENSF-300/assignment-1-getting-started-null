def addNums(a: int, b: int) -> int:
    sum_nums = a+b
    return sum_nums


def divideNums(a: int, b: int) -> int:
    quotient = a//b
    return quotient


def subtractNums(a: int, b: int) -> int:
    difference = a-b
    return difference


def multiplyNums(a: int, b: int) -> int:
    product = a*b
    return product


def getNumbersList(equation_list: list) -> list:
    return [(equation_list)[i] for i in range(len(equation_list)) if i % 2 == 0]


def getOperatorsList(equation_list: list) -> list:
    return [(equation_list)[i] for i in range(len(equation_list)) if i % 2 != 0]


def validateNumbers(numbers_list: list) -> list:
    try:
        integer_list = [int(x) for x in numbers_list]
        return integer_list
    except Exception as e:
        if "invalid literal for int() with base 10" in str(e):
            valid_input_list = input(
                "One or more of your numbers is invalid, enter an equation with 3 integer values and 2 operators separated by spaces:\n").split(" ")
            valid_numbers_list = getNumbersList(valid_input_list)
            validateNumbers(valid_numbers_list)
        else:
            raise e


def validateOperators(operators_list: list) -> None:
    valid_operators = ['+', '-', '*', '/']

    invalid_inputs = [x for x in operators_list if not (x in valid_operators)]

    if len(invalid_inputs) != 0:
        valid_input_list = input(
            "One or more of your operators is invalid, enter an equation with 3 integer values and 2 operators separated by spaces:\n").split(" ")
        valid_operators_list = getOperatorsList(valid_input_list)
        validateOperators(valid_operators_list)


def performCalculation(operators_list: list, numbers_list: list) -> int:
    operator_combo = "".join(operators_list)

    a, b, c = numbers_list[0], numbers_list[1], numbers_list[2]
    operations_dict = {
        "+-": subtractNums((addNums(a, b)), c),
        "-+": addNums((subtractNums(a, b)), c),
        "+/": addNums(a, (divideNums(b, c))),
        "/+": addNums((divideNums(a, b)), c),
        "+*": addNums(a, (divideNums(b, c))),
        "*+": addNums((multiplyNums(a, b)), c),
        "-/": subtractNums(a, (divideNums(b, c))),
        "/-": subtractNums((divideNums(a, b)), c),
        "*-": subtractNums((multiplyNums(a, b)), c),
        "-*": subtractNums(a, (multiplyNums(b, c))),
        "/*": multiplyNums((divideNums(a, b)), c),
        "*/": divideNums((multiplyNums(a, b)), c),
        "++": addNums((addNums(a, b)), c),
        "--": subtractNums((subtractNums(a, b)), c),
        "**": multiplyNums((multiplyNums(a, b)), c),
        "//": divideNums((divideNums(a, b)), c),
    }
    return operations_dict[operator_combo]


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


if __name__ == "__main__":
    main()
