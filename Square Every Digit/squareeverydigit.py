def square_digits(num):
    numArrays = list(str(num));
    squareDigits = ''
    for number in numArrays:
        squareDigits += str(int(number) ** 2)

    return int(squareDigits)
