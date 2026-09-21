class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
        self.cache = {}
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        prev.nxt = node
        node.nxt = nxt
        nxt.prev = node
    
    def remove(self, node: Node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru_key = self.left.nxt.key
            self.remove(self.cache[lru_key])
            del self.cache[lru_key]

        
