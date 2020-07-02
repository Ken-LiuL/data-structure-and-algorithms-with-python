class HashSet:
    class __Placeholder:
        def __init__(self):
            pass
        def __eq__(self):
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

