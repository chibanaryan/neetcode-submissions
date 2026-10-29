class Node:

    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt, self.right.prev = self.right, self.left
        self.cache = {}
    
    def insert(self, node: Node):
        prev, nxt = self.right.prev, self.right
        prev.nxt, nxt.prev = node, node
        node.prev, node.nxt = prev, nxt
    
    def remove(self, node: Node):
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].value = value
        else:
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                del self.cache[self.left.nxt.key]
                self.remove(self.left.nxt)
                
            
        
