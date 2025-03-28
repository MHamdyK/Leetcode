class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.next,self.prev = None,None
        
class LRUCache:

    def __init__(self, capacity: int):
        # this is a hashmap that stores keys along with the node that contains that key value pair.
        self.cache = {}
        self.cap = capacity
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left

    def removeNode(self,node):
        # get the previous and next Nodes of the current node
        prev,nxt = node.prev,node.next
        # previous node's next is the next of the current node
        prev.next = nxt
        # next node's prev is the prev of the current node
        nxt.prev = prev

    # add a node to the most right position
    def addNode(self,node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            # this method inserts the node at the right most position
            self.addNode(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        self.cache[key] = Node(key,value)
        self.addNode(self.cache[key])
        # Neeed to remove the left most Node
        if len(self.cache) > self.cap:
            # make sure that you assign the pointer to lru first, cuz removeNode function makes the left pointer points to the next node.
            lru = self.left.next
            self.removeNode(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)