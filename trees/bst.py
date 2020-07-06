class BinarySearchTree:
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val =  val
            self.left = left
            self.right = right

        #inorder traverse
        def __iter__(self):
            if self.left:
                for e in self.left:
                    yield e

            yield self.val

            if self.right:
                for e in self.right:
                    yield e
    def __init__(self):
        self.root = None

    def insert(self, val):
        def __insert(root, val):
            if root == None:
                return self.__Node(val)
            if val < root.val:
                root.left = __insert(root.left, val)
            else:
                root.right = __insert(root.right, val)
            return root
        self.root = __insert(self.root, val)
    
    def __iter__(self):
        if self.root:
            return self.root.__iter__()
        else:
            return [].__iter__()

if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(3)
    tree.insert(2)
    tree.insert(11)
    tree.insert(1)
    tree.insert(6)
    tree.insert(5)

    for n in tree:
        print(n)





