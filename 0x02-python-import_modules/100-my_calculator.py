#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        from calculator_1 import add, sub, mul, div
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        match sys.argv[2]:
            case '+':
                print("{} + {} = {}".format(a, b, a + b))
            case '-':
                print("{} - {} = {}".format(a, b, a - b))
            case '*':
                print("{} * {} = {}".format(a, b, a * b))
            case '/':
                print("{} / {} = {}".format(a, b, a / b))
            case _:
                print("Unknown operator. Available operators: +, -, * and /")
                sys.exit(1)
