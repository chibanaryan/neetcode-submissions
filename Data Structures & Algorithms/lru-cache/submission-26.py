class Node:

    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.nxt = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        node.nxt = nxt
        prev.nxt = node
        nxt.prev = node
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                lru_node = self.left.nxt
                self.remove(lru_node)
                del self.cache[lru_node.key]
        
