def main():
    """Demo function scope."""
    x = [3]
    print("in main, id is {}".format(id(x)))
    function(x)
    print("in main, id is {}".format(id(x)))


def function(y):
    print("in func, id is {}".format(id(y)))
    y += [1]
    print("in func, id is {}".format(id(y)))


main()
