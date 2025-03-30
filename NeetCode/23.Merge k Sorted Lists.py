# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwo(head1,head2):
    dummy = ListNode()
    curr_head = dummy

    while head1 is not None and head2 is not None:

        # check which node is smaller and merge them
        if head1.val <= head2.val:
            curr_head.next = head1
            head1 = head1.next
        else:
            curr_head.next = head2
            head2 = head2.next

        curr_head = curr_head.next
        # Condition if head1 is greater than l2 or the opposite
    if head1 is not None:
        curr_head.next = head1
    else:
        curr_head.next = head2
    return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        for head in lists:
            result = mergeTwo(result,head)
        return result
