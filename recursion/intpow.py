def intpow(x, n):
    """[compute x ^ n recursively]
    Args:
        x ([int]): [base]
        n ([int]): [index]
    """
    if n == 0:
        return 1
    return x * intpow(x, n - 1)


assert(intpow(2, 3) == 8)
assert(intpow(3, 2) == 9)

    