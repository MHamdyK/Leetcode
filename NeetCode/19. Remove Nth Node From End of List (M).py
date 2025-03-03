class Solution:
    def removeNthFromEnd(self, head:Optional[ListNode], n:int)-> Optional[ListNode]:
        #first get the length of the list
        length = 0
        curr_node = head
        while curr_node:
            length+= 1
            curr_node = curr_node.next
        # get the real index of the element you want to remove from left to right
        target_index = length - n
        counter = 0
        #if you want to remove the first index, simple!
        if target_index == 0:
            head = head.next
            return head
        curr_node = head
        prev = curr_node
        while counter != target_index:
            prev = curr_node
            curr_node = curr_node.next
            counter += 1
        prev.next = curr_node.next
        return head
