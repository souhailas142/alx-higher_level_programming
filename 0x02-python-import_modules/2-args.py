#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_argv = len(sys.argv) - 1
    i = 1
    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    elif len_argv == 1:
        print("{}: argument:".format(len_argv))
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len_argv))
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1
