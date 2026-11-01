# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        sum1 = sum2 = 0
        multiplier = 1 
        while l1:
            sum1 += l1.val*multiplier
            multiplier *= 10
            l1=l1.next
        
        #reset multiplier
        multiplier = 1 
        while l2:
            sum2 += l2.val*multiplier
            multiplier *= 10
            l2=l2.next

        new_sum = sum1+sum2
        dummy = ListNode(0)
        curr = dummy 

        while new_sum > 0:
            digit = new_sum % 10
            curr.next = ListNode(digit)
            curr = curr.next
            new_sum //= 10

        return dummy.next if dummy.next else ListNode(0)