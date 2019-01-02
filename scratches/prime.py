# encoding:utf-8

def get_primes(n):
    primes = [2]
    l_odds = [i for i in range(3, n + 1) if i % 2 == 1]
    for l_odd in l_odds:
        c = 0
        for prime in primes:
            if l_odd % prime == 0:
                continue
            else:
                c += 1
            if c == len(primes):
                primes.append(l_odd)
    print(primes)
 
get_primes(10 ** 3)
