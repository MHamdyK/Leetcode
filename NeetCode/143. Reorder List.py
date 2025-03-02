# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the first and second halfs of the list
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # first node in the second half
        second = slow.next
        prev = slow.next = None

        # Reversing for the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge the Two lists
        # after finishing the loop that reverse the second half, Now "second" is looking at None, which is what the LAST node is looking at
        # `prev` is indeed the last node before second
        first,second = head,prev
        while second:
            # store the node, first half was looking at before merging
            temp1 = first.next
            first.next = second
            # store the node, second half was looking at before merging
            temp2 = second.next
            second.next = temp1
            # shift each node, to the node it was looking at before
            first = temp1 
            second = temp2

