#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        rslt = fct(*args)
        return rslt
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
