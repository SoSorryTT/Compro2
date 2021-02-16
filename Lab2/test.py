def RecCountup(n):
    """
    Prints the numbers from 0 to `n`.

    Examples:
        >>> RecCountup(0)
        0

        >>> RecCountup(7)
        0
        1
        2
        3
        4
        5
        6
        7

    """
    if n == 0:
        return print('0')
    RecCountup(n - 1)
    print(n)

RecCountup(7)