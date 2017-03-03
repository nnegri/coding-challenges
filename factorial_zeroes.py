# Take the number that you've been given the factorial of.
# Divide by 5; if you get a decimal, truncate to a whole number.
# Divide by 52 = 25; if you get a decimal, truncate to a whole number.
# Divide by 53 = 125; if you get a decimal, truncate to a whole number.
# Continue with ever-higher powers of 5, until your division results in a number less than 1. Once the division is less than 1, stop.
# Sum all the whole numbers you got in your divisions. This is the number of trailing zeroes.


def factorial_zeroes(n):
    zeroes = []
    x=1
    while True:
        if n/(5**x) < 1:
            break
        zeroes.append(n/(5**x))
        x += 1
    return sum(zeroes)

print factorial_zeroes(4617)