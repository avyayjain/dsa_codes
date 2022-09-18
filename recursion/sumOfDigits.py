def sumOfDigits(n):
    if n == 0:
        return n
    else:
        n+sumOfDigits(n-1)

sumOfDigits(10)
