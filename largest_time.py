# Given a set of integers, what's the largest 24 hour time you can represent out of them?  

# if 2 is in list and another number 3 or less, append to string
    # if 3 in list, append.. elif 2..1..0

# elif 1 in list, append to string
    # if 9 in list, append.. elif 8...

# if 5 in list.. elif 4....
    #if 9 in list... elif 8..

# [2,5,6,9,1,2] --> 22:59


def largest_time(digits):
    output = ""

    if 2 in digits:
        digits.remove(2)
        output += "2"

        for i in range(3, -1, -1):
            if i in digits:
                digits.remove(i)
                output += str(i)
                break

    elif 1 in digits:
        digits.remove(1)
        output += "1"

        for i in range(9, -1, -1):
            if i in digits:
                digits.remove(i)
                output += str(i)
                break

    elif 0 in digits:
        digits.remove(0)
        output += "0"

        for i in range(9, -1, -1):
            if i in digits:
                digits.remove(i)
                output += str(i)
                break

    output += ":"

    for i in range(5,-1,-1):
        if i in digits:
            digits.remove(i)
            output += str(i)
            break

    for i in range(9,-1,-1):
        if i in digits:
            digits.remove(i)
            output += str(i)
            break

    return output

print largest_time([2,5,6,9,1,2])