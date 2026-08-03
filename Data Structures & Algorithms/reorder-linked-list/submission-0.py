# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 1
        temp = head

        while temp.next:
            length += 1
            temp = temp.next
        
        h2 = head

        for i in range(int(length/2)):
            h2 = h2.next

        prev = None
        curr = h2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        h2 = prev
        h1 = head

        while h2.next:
            temp2 = h2.next
            temp1 = h1.next

            h1.next = h2
            h2.next = temp1
            h1 = temp1
            h2 = temp2
            
        




