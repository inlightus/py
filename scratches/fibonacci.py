# encoding: utf-8

def fib(n):
    a, b = 1, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fib(2000)


def fibo(n):
    a, b = 1, 1

    seq = []

    while a < n:
        seq.append(a)
        a, b = b, a + b

    print(*seq)

fibo(2000)
