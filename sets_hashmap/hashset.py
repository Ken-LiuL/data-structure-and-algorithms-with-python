class HashSet:
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self, v):
            return False
    def __init__(self, contents=[]):
        self.items = [None] * 10
        self.size =  0
        for item in contents:
            self.add(item)

    #linear probing
    @classmethod
    def __add(cls, item, items):
        idx = hash(item) % len(items)
        while items[idx] != None:
            if items[idx] == item:
                return False
            if type(items[idx]) == HashSet.__Placeholder:
                items[idx] = item
                break
            idx = (idx + 1) % len(items)

        items[idx] = item
        return True

    @classmethod
    def __rehash(cls, oldlist, newlist):
        for x in oldlist:
            if x != None and type(x) != HashSet.__Placeholder:
                cls.__add(x, newlist)
    
    def add(self, item):
        if self.__add(item, self.items):
            self.size += 1
            load = self.size / len(self.items) 
            if load >= 0.75:
                self.items = self.__rehash(self.items, [None]*2*len(self.items))
    
    @classmethod
    def __remove(cls, item, items):
        idx = hash(item) % len(items)
        while items[idx] != None:
            if items[idx] == item:
                next_idx = (idx + 1) % len(items)
                if items[next_idx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet.__Placeholder()
                return True
            idx = (idx + 1) % len(items)
        return False
    
    def remove(self, item):
        if self.__remove(item, self.items):
            self.size -= 1
            load = max(self.size, 10) / len(self.items)
            if load <= 0.25:
                self.items = self.__rehash(self.items, [None]*int(len(self.items) / 2))
        else:
            raise KeyError('Item not found')
    
    def __contains__(self, item):
        idx = hash(item) % len(self.items)
        while self.items[idx]  != None:
            if self.items[idx] == item:
                return True
            idx = (idx + 1) % len(self.items)
        return False
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet.__Placeholder:
                yield self.items[i]
    
    def __getitem__(self, item):
        if  item in self:
            idx = hash(item) % len(self.items)
            while self.items[idx] != None:
                if self.items[idx] == item:
                    return self.items[idx]
                idx = (idx + 1) %len(self.items)
            return  None
        else:
            None
            
    
    def difference(self, other):
        result = HashSet(self)
        result.difference_update(other)
        return result
    
    def discard(self, item):
        if item in self:
            self.remove(item)
    
    def difference_update(self, other):
        for item in other:
            self.discard(item)
    

