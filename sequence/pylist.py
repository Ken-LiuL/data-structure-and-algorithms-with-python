class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None]*size
        self.size = 0
        self.capacity = size
        for e in contents:
            self.append(e)
    
    def __getitem__(self, ind):
        if ind < self.size:
            return self.items[ind % self.size]
        else:
            raise IndexError('Invalid index {}'.format(ind))

    def __setitem__(self, ind, val):
        if ind < self.size:
            self.items[ind % self.size] = val
        else:
            raise IndexError('Invalid index {}'.format(ind))
    
    def __iter__(self):
        for i in range(self.size):
            yield self.items[i]
    
    def __add__(self, other):
        res = PyList(size=self.size + other.size)
        for e in self:
            res.append(e)
        for e in other:
            res.append(e)
        return res
    
    def _enlarge(self):
        newcap = (self.capacity // 4) + self.capacity + 1
        newlst = [None] * newcap
        for i in range(self.capacity):
            newlst[i] = self.items[i]
        
        self.items = newlst
        self.capacity = newcap

    def __delitem__(self, ind):
        for i in range(ind, self.size-1):
            self[i] = self[i+1]
        self.size -= 1
    
    def __len__(self):
        return  self.size
    
    def __contains__(self, item):
        for e in self:
            if e == item:
                return True
        return False
    
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.size != other.size:
            return False
        for i in range(self.size):
            if   self[i] != other[i]:
                return False
        return True
    
    def __str__(self):
        return ','.join([str(e) for e in self])

    def insert(self, i, e):
        if self.capacity == self.size:
            self._enlarge()
        if i < self.size:
            for j in range(self.size-1, i-1, -1):
                self[j+1] = self[j]
            self[i] = e
            self.size += 1

        else:
            self.append(e)

    def append(self, e):
        if self.size == self.capacity:
            self._enlarge()
        self.items[self.size] = e
        self.size += 1

if __name__ == '__main__':
    a= PyList(contents=['a','b','c'])
    b = PyList(contents=[1,2,3])
    for e in a+b:
        print(e)

    print( 1 in b)
    print(b)
         
