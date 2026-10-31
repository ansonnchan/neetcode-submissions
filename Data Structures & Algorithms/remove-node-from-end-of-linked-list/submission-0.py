# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        count = 0
        curr = head
        curr2 = head

        while curr:
            count += 1
            curr = curr.next

        complement = count - n

        if complement == 0:
            return head.next

        # Move to the node BEFORE the one to remove
        for _ in range(complement - 1):
            curr2 = curr2.next

        # Skip the node to remove
        curr2.next = curr2.next.next

        return head

