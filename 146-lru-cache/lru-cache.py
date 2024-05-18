class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache= {}

        # left -> LRU, right -> MRU
        self.left, self.right = ListNode(), ListNode()
        self.left.next = self.right
        self.right.prev = self.left
    
    # removes from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    # inserts to MRU, right of doubly LL
    def insert(self, node):
        curr = node
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        nxt.prev = node

        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # remove and add key to MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove from list & cache
            self.remove(self.cache[key])
        
        # always add
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        # if over cacpcity, remove from LRU
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)