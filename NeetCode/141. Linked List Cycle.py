class Solution:
    def hasCycle(self,head: Optional[ListNode]) -> bool:
        visited_nodes = []
        curr_node = head
        # if Linked List is empty
        if not curr_node:
            return False
        while True:
            if curr_node.next == None:
                return False
            if curr_node in visited_nodes:
                return True
            visited_nodes.append(curr_node)
            curr_node = curr_node.next
                
