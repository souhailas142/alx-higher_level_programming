#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    len_arg = len(sys.argv) - 1
    if len_arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        opt = sys.argv[2]
        b = int(sys.argv[3])
        if opt == "+":
            print("{} {} {} = {}".format(a, opt, b, add(a, b)))
        elif opt == "-":
            print("{} {} {} = {}".format(a, opt, b, sub(a, b)))
        elif opt == "*":
            print("{} {} {} = {}".format(a, opt, b, mul(a, b)))
        elif opt == "/":
            print("{} {} {} = {}".format(a, opt, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
