def pow(x=1):
    """
    Returns x * x
    :param x: float.
    :return: float square of x.
    """
    try:
        x = input("type a number: ")
        x = float(x)
        return x * x
    except ValueError:
        print("Invalid input")

first = pow()
print(first)

second = pow()
print(second)

third = pow()
print(third)

fourth = pow()
print(fourth)
