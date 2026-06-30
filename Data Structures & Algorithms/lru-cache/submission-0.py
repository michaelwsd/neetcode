class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.storage = {}
        self.lru, self.mru = Node(), Node()
        self.lru.right, self.mru.left = self.mru, self.lru

    def insert(self, key, node):
        self.storage[key] = node
        self.mru.left.right, node.left = node, self.mru.left
        node.right, self.mru.left = self.mru, node

    def delete(self, key):
        node = self.storage[key]
        node.left.right = node.right
        node.right.left = node.left
        del self.storage[key]

    def get(self, key: int) -> int:
        if key not in self.storage: return -1
        node = self.storage[key]
        self.delete(key)
        self.insert(key, node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.storage: 
            self.delete(key)

        self.insert(key, Node(key, value))
        if len(self.storage) > self.capacity:
            evict = self.lru.right
            self.lru.right = evict.right
            evict.right.left = self.lru
            del self.storage[evict.key]
        

        
