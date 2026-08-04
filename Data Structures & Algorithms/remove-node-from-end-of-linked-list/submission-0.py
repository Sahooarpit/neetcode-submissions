# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 1

        node = head

        while node:
            length +=1
            node = node.next
        
        pos = length - n -1

        node = ListNode()
        node.next = head
        head = node

        for i in range(pos):
            node = node.next
        
        node.next = node.next.next

        return head.next
        
        
        
