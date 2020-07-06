from hashset import HashSet
class HashMap:
    class __KVPair:
        def __init__(self, k, v):
            self.k = k
            self.v = v
        
        def __eq__(self, other):
            if type(self) != type(other):
                return False
            return self.k == other.k
        
        def __hash__(self):
            return hash(self.k)
        
    def __init__(self):
        self.hset = HashSet()
    
    def __len__(self):
        return len(self.hset)
    
    def __contains__(self, item):
        return self.__KVPair(item, None) in self.hset
    
    def not__contains__(self, item):
        return item not in self.hset
    
    def __setitem__(self, k, v):
        self.hset.add(self.__KVPair(k, v))
    
    def __getitem__(self, k):
        if self.__KVPair(k, None) in self.hset:
            return self.hset[self.__KVPair(k, None)].v
        raise KeyError('key {} not in hashmap'.format(k))
    
    def __iter__(self):
        for x in self.hset:
            yield x.k


        