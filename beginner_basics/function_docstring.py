# Biwott
# Docstring


def print_max(x, y):
    '''Prints the maximum of two numbers.
    Must be integers'''

    # convert to integers
    x = int(x)
    y = int(y)

    if x > y:
        print ('Maximum is :', 8)
    else:
        print (y, 'Is maximum')


print_max(8, 5)
print(print_max.__doc__)        # Doc String
