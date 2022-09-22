def addNums(a, b):
    return a + b


def divideNums(a, b):
    return a/b


def subtractNums(a, b):
    return a-b


def multiplyNums(a, b):
    return a*b


def performCalculation(a, b, c, operator1, operator2):
    operators = operator1 + operator2
    operations_dict = {
        "+-": subtractNums(addNums(a, b), c),
        "-+": addNums(subtractNums(a, b), c),
        "+/": addNums(a, divideNums(b, c)),
        "/+": addNums(divideNums(a, b), c),
        "+*": addNums(a, divideNums(b, c)),
        "*+": addNums(multiplyNums(a, b), c),
        "-/": subtractNums(a, divideNums(b, c)),
        "/-": subtractNums(divideNums(a, b), c),
        "*-": subtractNums(multiplyNums(a, b), c),
        "-*": subtractNums(a, multiplyNums),
        "/*": multiplyNums(divideNums(a, b), c),
        "*/": divideNums(multiplyNums(a, b), c),
        "++": addNums(addNums(a, b), c),
        "--": subtractNums(subtractNums(a, b), c)
    }
    return operations_dict[operators]


def main():

    print(performCalculation(1, 2, 2, '+', "/"))
