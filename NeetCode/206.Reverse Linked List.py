class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        curr_node = head
        while curr_node != null:
            next_node = curr_node.next
            curr_node.next = previous_node
            previous_node = curr_node
            curr_node = next_node
        
        return previous_node
