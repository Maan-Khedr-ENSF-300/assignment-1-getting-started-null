from calculateNums import *
from validateInputs import *


def unitTests() -> None:
    # tests for myAdd() function
    assert myAdd(5, 2) == 7
    assert myAdd(0, -5) == -5
    assert myAdd(-100000, 2) == -99998
    assert myAdd(-55, -21) == -76

    # tests for mySubract()
    assert mySubtract(5, 2) == 3
    assert mySubtract(0, -5) == 5
    assert mySubtract(-100000, 2) == -100002
    assert mySubtract(-55, -21) == -34

    # tests for myMultiply()
    assert myMultiply(5, 2) == 10
    assert myMultiply(1, -5) == -5
    assert myMultiply(-100000, 2) == -200000
    assert myMultiply(-55, -21) == 1155

    # tests for myDivide()
    assert myDivide(5, 2) == 2
    assert myDivide(1, -5) == 0
    assert myDivide(-100000, 2) == -50000
    assert myDivide(-55, -21) == 2

    # tests for performCalculation() for each key in "operations_dict"
    assert performCalculation(["+", "+"], [6, 9, 20]) == 35
    assert performCalculation(["-", "-"], [10, 15, -2]) == -3
    assert performCalculation(["*", "*"], [6, 9, 3]) == 162
    assert performCalculation(["/", "/"], [23, 4, 2]) == 2
    assert performCalculation(["+", "-"], [23, 4, -5]) == 32
    assert performCalculation(["-", "+"], [23, 4, -5]) == 14
    assert performCalculation(["+", "*"], [14, 5, 3]) == 29
    assert performCalculation(["*", "+"], [14, 5, 3]) == 73
    assert performCalculation(["*", "/"], [35, 3, 14]) == 7
    assert performCalculation(["/", "*"], [35, 3, 14]) == 154
    assert performCalculation(["/", "+"], [10, 3, 18]) == 21
    assert performCalculation(["+", "/"], [10, 103, -7]) == -4
    assert performCalculation(["/", "-"], [50, 4, 4]) == 8
    assert performCalculation(["-", "/"], [50, 40, 5]) == 42
    assert performCalculation(["-", "*"], [45, 10, -4]) == 85
    assert performCalculation(["*", "-"], [5, 15, 75]) == 0

    # tests for getNumbersList() **numbers are in string format by default for user input**
    assert getNumbersList(["15", "+", "6", "-", "17"]) == ["15", "6", "17"]
    assert getNumbersList(["29", "/", "3", "+", "18"]) == ["29", "3", "18"]
    assert getNumbersList(["1", "-", "1", "-", "2"]) == ["1", "1", "2"]
    assert getNumbersList(["22", "+", "16", "-", "3"]) == ["22", "16", "3"]

    # tests for getOperatorsList() **numbers are in string format by default for user input**
    assert getOperatorsList(["15", "+", "6", "-", "17"]) == ["+", "-"]
    assert getOperatorsList(["29", "/", "3", "+", "18"]) == ["/", "+"]
    assert getOperatorsList(["1", "-", "1", "-", "2"]) == ["-", "-"]
    assert getOperatorsList(["22", "*", "16", "-", "3"]) == ["*", "-"]

    # tests for validateNumbers()
    assert validateNumbers(["15", "6", "17"]) == [15, 6, 17]
    assert validateNumbers(["10", "5", "0"]) == [10, 5, 0]
    assert validateNumbers(["-15", "-3", "2"]) == [-15, -3, 2]
    assert validateNumbers(["1", "2", "-50"]) == [1, 2, -50]

    # tests for validateOperators()
    assert validateOperators(["+", "+"]) == True
    assert validateOperators(["-", "-"]) == True
    assert validateOperators(["*", "*"]) == True
    assert validateOperators(["/", "/"]) == True
    assert validateOperators(["+", "-"]) == True
    assert validateOperators(["-", "+"]) == True
    assert validateOperators(["+", "*"]) == True
    assert validateOperators(["*", "+"]) == True
    assert validateOperators(["*", "/"]) == True
    assert validateOperators(["/", "*"]) == True
    assert validateOperators(["/", "+"]) == True
    assert validateOperators(["+", "/"]) == True
    assert validateOperators(["/", "-"]) == True
    assert validateOperators(["-", "/"]) == True
    assert validateOperators(["-", "*"]) == True
    assert validateOperators(["*", "-"]) == True


def integrationTests() -> None:

    """
    These are the integration tests. Since no testing framework was used,
    we could not simply do the tests by testing the main function due to 
    the input buffer so these function calls follow the logic of the program.
    """
    assert displayUserExpression((validateNumbers(getNumbersList(["4", "+", "3", "+", "2"]))),
    (getOperatorsList(["4", "+", "3", "+", "2", "="])), performCalculation(["+", "+"], [4, 3, 2])) == "4 + 3 + 2 = \n9"

    assert displayUserExpression((validateNumbers(getNumbersList(["8", "-", "3", "-", "2"]))),
    (getOperatorsList(["8", "-", "3", "-", "2", "="])), performCalculation(["-", "-"], [8, 3, 2])) == "8 - 3 - 2 = \n3"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "*", "3", "*", "2"]))),
    (getOperatorsList(["4", "*", "3", "*", "2", "="])), performCalculation(["*", "*"], [4, 3, 2])) == "4 * 3 * 2 = \n24"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "/", "1", "/", "2"]))),
    (getOperatorsList(["4", "/", "1", "/", "2", "="])), performCalculation(["/", "/"], [4, 1, 2])) == "4 / 1 / 2 = \n2"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "+", "3", "-", "2"]))),
    (getOperatorsList(["4", "+", "3", "-", "2", "="])), performCalculation(["+", "-"], [4, 3, 2])) == "4 + 3 - 2 = \n5"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "-", "3", "+", "2"]))),
    (getOperatorsList(["4", "-", "3", "+", "2", "="])), performCalculation(["-", "+"], [4, 3, 2])) == "4 - 3 + 2 = \n3"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "+", "3", "*", "2"]))),
    (getOperatorsList(["4", "+", "3", "*", "2", "="])), performCalculation(["+", "*"], [4, 3, 2])) == "4 + 3 * 2 = \n14"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "*", "3", "+", "2"]))),
    (getOperatorsList(["4", "*", "3", "+", "2", "="])), performCalculation(["*", "+"], [4, 3, 2])) == "4 * 3 + 2 = \n14"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "*", "3", "/", "2"]))),
    (getOperatorsList(["4", "*", "3", "/", "2", "="])), performCalculation(["*", "/"], [4, 3, 2])) == "4 * 3 / 2 = \n6"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "/", "1", "*", "2"]))),
    (getOperatorsList(["4", "/", "1", "*", "2", "="])), performCalculation(["/", "*"], [4, 1, 2])) == "4 / 1 * 2 = \n8"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "/", "1", "+", "2"]))),
    (getOperatorsList(["4", "/", "1", "+", "2", "="])), performCalculation(["/", "+"], [4, 1, 2])) == "4 / 1 + 2 = \n6"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "+", "3", "/", "1"]))),
    (getOperatorsList(["4", "+", "3", "/", "1", "="])), performCalculation(["+", "/"], [4, 3, 1])) == "4 + 3 / 1 = \n7"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "/", "2", "-", "1"]))),
    (getOperatorsList(["4", "/", "2", "-", "1", "="])), performCalculation(["/", "-"], [4, 2, 1])) == "4 / 2 - 1 = \n1"

    assert displayUserExpression((validateNumbers(getNumbersList(["11", "-", "3", "/", "2"]))),
    (getOperatorsList(["11", "-", "3", "/", "2", "="])), performCalculation(["-", "/"], [11, 3, 2])) == "11 - 3 / 2 = \n4"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "-", "3", "*", "2"]))),
    (getOperatorsList(["4", "-", "3", "*", "2", "="])), performCalculation(["-", "*"], [4, 3, 2])) == "4 - 3 * 2 = \n2"

    assert displayUserExpression((validateNumbers(getNumbersList(["4", "*", "3", "-", "2"]))),
    (getOperatorsList(["4", "*", "3", "-", "2", "="])), performCalculation(["*", "-"], [4, 3, 2])) == "4 * 3 - 2 = \n10"