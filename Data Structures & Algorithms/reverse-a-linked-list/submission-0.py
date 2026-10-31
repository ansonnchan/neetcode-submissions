# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #1->2->3->4->5
        #2->1
        #5->4->3->2->1
        curr, prev = head, None

        while curr is not None:
            next_node = curr.next #->1
            curr.next = prev #->None
            prev = curr 
            curr = next_node
        return prev 


        
        