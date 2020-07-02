class LinkedList:
    class __Node:
        def __init__(self, item, next=None):
            self.item = item
            self.next = next
    
    def __getitem__(self, index):
        if index < self.size:
            cursor = self.first.next
            for _ in range(index % self.size):
                cursor = cursor.next
            return cursor.item
        else:
            raise IndexError('Invalid index {}'.format(index))
    def __setitem__(self, index, val):
        if index < self.size:
            cursor = self.first.next
            for _ in range(index % self.size):
                cursor = cursor.next
            return cursor.item
        else:
            raise IndexError('Invalid index {}'.format(index))
    
    def __add__(self, other):
        if type(self) != type(other):
            raise TypeError('Concatenate undefined for {} + {}'.format(str(type(self)), str(type(other))))
    
        res = LinkedList()    
        cursor = self.first.next

        while cursor != None:
            res.append(cursor.item)
            cursor = cursor.next
        cursor = other.first.next

        while cursor != None:
            res.append(cursor.item)
            cursor = cursor.next
        
        return res

    def __init__(self, contents = []):
        #Dummy node
        self.first = LinkedList.__Node(None, None)
        self.last = self.first
        self.size = 0
        for e in contents:
            self.append(e)
    
    def append(self, item):
        node = LinkedList.__Node(item)
        self.last.next = node
        self.last = node
        self.size += 1
    
    def insert(self, index, item):
        cursor = self.first.next
        if index < self.size:
            for _ in range(index):
                cursor = cursor.next
            node = LinkedList.__Node(item, cursor.next)
            cursor.next = node
            self.size += 1
        else:
            self.append(item)

    def __contain__(self, item):
        cursor = self.first.next
        while cursor != None:
            if cursor.item == item:
                return True
            cursor = cursor.next

    def __str__(self):
        return ','.join([str(i) for i in self])
    def __iter__(self):
        cursor = self.first.next
        while cursor != None:
            yield cursor.item
            cursor = cursor.next
        
if __name__ == '__main__':
    a= LinkedList(contents=['a','b','c'])
    b = LinkedList(contents=[1,2,3])
    for e in a+b:
        print(e)

    print( 1 in b)
    print(b)
         

        
    
    


