def gcd(number1, number2):
    while True:
        big = max(number1, number2)
        small = min(number1, number2)

        remainder = big % small
        if remainder == 0:
            return small
        else:
            number1 = remainder
            number2 = small