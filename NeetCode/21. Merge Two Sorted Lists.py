# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None: 
            return list1
        curr_node = list1 if (list1.val<=list2.val) else list2
        head = list1 if (list1.val<=list2.val) else list2
        p1 = curr_node.next
        p2 = list2 if (list1.val<=list2.val) else list1
        if p1 == None:
            curr_node.next = p2
        flag1 = 0
        flag2 = 0
        while p1 != None and p2 != None:
            # if your next is your actual next
            if p1.val <= p2.val:
                curr_node.next = p1
                curr_node = p1
                p1 = p1.next
                if p1 == None:
                    curr_node.next = p2
            # this means that we should change paths
            else:
                curr_node.next = p2
                curr_node = p2
                p2 = p2.next
                if p2 == None: 
                    curr_node.next = p1
        return head