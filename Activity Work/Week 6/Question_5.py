class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):    # Remove node from linked list
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):   # Add node right after head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:    # Remove LRU from linked list and dict
                lru = self.tail.prev
                self._remove(lru)

                self.cache.pop(lru.key)

            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add(new_node)


# Example usage:
command = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"] 
value = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] 

lru_cache = None
for a, b in zip(command, value):
    if a == "LRUCache":
        lru_cache = LRUCache(*b)
        print("null")
    elif a == "put":
        lru_cache.put(*b)
        print("null")
    elif a == "get":
        result = lru_cache.get(*b)
        print(result)