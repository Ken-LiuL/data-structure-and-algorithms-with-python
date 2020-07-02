def revlist(lst):
    head, *tail = lst
    if tail == []:
        return [head] 
    return revlist(tail) + [head]


def revstr(s):
    head, *tail = s
    if tail == []:
        return head
    return revstr(tail) + head

def rev(s):
    empty_ele = type(s)()
    def revhelper(s):
        if s == empty_ele:
            return empty_ele
        first = s[0:1]
        return revhelper(s[1:]) + first
    return revhelper(s)
    
print(revlist([1,2,3,4]))
print(revstr('abcd'))
print(rev([1,2,3]))
print(rev('hello'))
        