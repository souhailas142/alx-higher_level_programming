#!/urs/bin/python3
def safe_print_list(my_list=[], x=0):
    _len = 0
    for item in my_list:
        _len += 1
    for index, item in enumerate(my_list):
        if x == index:
            break
        print(item, end="")
    print()
    return (_len if (x > _len) else x)
