def length_of_str(s):
    if s == '':
        return 0
    return 1 + length_of_str(s[1:])

if __name__ == '__main__':
    s = input('plz give a string\n')
    print('the length of {} is {}'.format(s, length_of_str(s)))
    
