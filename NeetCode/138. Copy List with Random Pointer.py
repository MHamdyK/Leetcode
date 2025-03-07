"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr_node = head
        oldToNew = {None:None}
        
        # first copy the old ListNode
        while curr_node:
            copy = Node(curr_node.val)
            oldToNew[curr_node] = copy
            curr_node = curr_node.next 

        # start linking nodes

        curr_node = head

        while curr_node:
            copy = oldToNew[curr_node]
            copy.next = oldToNew[curr_node.next]
            copy.random = oldToNew[curr_node.random]
            curr_node = curr_node.next
        return oldToNew[head]

