def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)


if __name__ == '__main__':
    n = input('plz give a number:\n')
    print('the factorial of {} is {}\n'.format(n, fac(int(n))))