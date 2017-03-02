

def change_combo(lst, output=None):
    """

    >>> change_combo([10, 2, 3])
    [12, 13, 5]

    >>> change_combo([1, 4, 9, 5])
    [5, 10, 6, 13, 9, 14]

    """
    if lst:
        if output == None:
            output = []

        for coin in lst[1:]:
            output.append(coin + lst[0])

        return change_combo(lst[1:], output)
        
    return output

print change_combo([10, 2, 3])
print change_combo([1, 4, 9, 5])
