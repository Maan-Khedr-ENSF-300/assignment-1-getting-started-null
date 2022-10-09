# receives 2 integers and returns the sum as an integer
def myAdd(a: int, b: int) -> int:
    sum_nums = a+b
    return sum_nums

# receives 2 integers and returns the quotient as an integer
def myDivide(a: int, b: int) -> int:
    quotient = a//b
    return quotient

# receives 2 integers and returns the difference as an integer
def mySubtract(a: int, b: int) -> int:
    difference = a-b
    return difference

# receives 2 integers and returns the product as an integer
def myMultiply(a: int, b: int) -> int:
    product = a*b
    return product

# receives a list of operators and a list of numbers parsed from the user input and returns the final answer
def performCalculation(operators_list: list, numbers_list: list) -> int:
    operator_combo = "".join(operators_list)

    a, b, c = numbers_list[0], numbers_list[1], numbers_list[2]

    # created dictionary for the combinations of operators instead of 16 "if/elif/else" statements
    operations_dict = {
        "+-": mySubtract((myAdd(a, b)), c),
        "-+": myAdd((mySubtract(a, b)), c),
        "+/": myAdd(a, (myDivide(b, c))),
        "/+": myAdd((myDivide(a, b)), c),
        "+*": myAdd(a, (myMultiply(b, c))),
        "*+": myAdd((myMultiply(a, b)), c),
        "-/": mySubtract(a, (myDivide(b, c))),
        "/-": mySubtract((myDivide(a, b)), c),
        "*-": mySubtract((myMultiply(a, b)), c),
        "-*": mySubtract(a, (myMultiply(b, c))),
        "/*": myMultiply((myDivide(a, b)), c),
        "*/": myDivide((myMultiply(a, b)), c),
        "++": myAdd((myAdd(a, b)), c),
        "--": mySubtract((mySubtract(a, b)), c),
        "**": myMultiply((myMultiply(a, b)), c),
        "//": myDivide((myDivide(a, b)), c),
    }
    return operations_dict[operator_combo]

# Takes 2 lists, loops though them and concatenates the expression together and prints output to terminal
def displayUserExpression(list_of_numbers: list, list_of_operators: list, final_answer: list) -> None:
    final_output = ""

    for i in range(len(list_of_numbers)):
        final_output += f"{list_of_numbers[i]} {list_of_operators[i]} "

    final_output += f"\n{final_answer}"
    print(final_output)