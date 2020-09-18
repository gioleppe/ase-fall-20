# calculator.py


def sum(m, n):
    if n >= 0:
        for el in range(n):
            m += 1
    else:
        for el in range(abs(n)):
            m -= 1
    return m


def divide(m, n):
    res = 0
    isNegative = m > 0 and n < 0 or m < 0 and n > 0
    n = abs(n)
    m = abs(m)
    while m >= n:
        m -= n
        res += 1

    res = -res if isNegative else res
    return res

