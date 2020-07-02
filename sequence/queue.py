class Queeu:
    def __init__(self):
        self.items = []
        self.front_ind = 0

    def empty(self):
        return self.front_ind == len(self.items)
        
    def __compress(self):
        newlst = []
        for i in range(self.front_ind, len(self.items)):
            newlst.append(self.items[i])
        self.items = newlst
        self.front_ind = 0

    def dequeue(self):
        if self.empty():
            raise RuntimeError('Attempt to dequeue an empty queue')
        if self.front_ind * 2 > len(self.items):
            self.__compress()
        item = self.items[self.front_ind]
        self.front_ind += 1
        return item

    def enqueue(self, item):
        self.items.append(item)