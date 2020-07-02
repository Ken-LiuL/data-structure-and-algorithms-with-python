def swap(s):
    p = s[0:2]
    if len(p) < 2:
        return p
    return p[1]+p[0]+swap(s[2:])


if __name__ == '__main__':
    s = input('plz give a string\n')
    print('the swap result of string {} is {}'.format(s, swap(s)))