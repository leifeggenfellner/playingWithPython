def largestPrimeFactor(n=600851475143):

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n /= 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(int(i))
            n /= i
        else:
            i += 2

    if n != 1:
        factors.append(int(n))

    return max(factors)
