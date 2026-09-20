class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key to node
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def remove(self, node: Node):
        # print("removals")
        # print(node.key, node.val)
        # print(node.prev.key, node.prev.val)
        # print (node.nxt.key, node.nxt.val)
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
    
    def insert(self, node: Node):
        self.right.prev.nxt = node
        node.prev = self.right.prev
        node.nxt = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        # print(f'get {key}')
        # print(self.cache)
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # print(f'put {key} {value}')
        # print(self.cache)
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru_key = self.left.nxt.key
            # print (f"removing {str(lru_key)}" )
            self.remove(self.cache[lru_key])
            del self.cache[lru_key]

        
