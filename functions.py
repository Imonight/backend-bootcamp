def isEven(n):
    return n % 2 == 0


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial1(n):
    i = 1
    result = 1
    while i <= n:
        result *= i
        i + 1
    return result
