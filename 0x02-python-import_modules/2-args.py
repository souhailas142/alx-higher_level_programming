#!/usr/bin/python3
import sys
if __name__ == "__main__":
    len_argv = len(sys.argv) - 1
    i = 1
    if len_argv == 0:
        print("{} arguments.".format(len_argv))
    else:
        print("{} argument{}:".format(len_argv, "" if len_argv == 1 else "s"))
        for av in sys.argv[1:]:
            print("{}: {}".format(i, av))
            i += 1
