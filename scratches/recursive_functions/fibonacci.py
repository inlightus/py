def fibonacci(n):
    if n == 1:
        return n
    if n == 0:
        return n

    print("Recursive call with {0} as input".format(n))
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(5)
