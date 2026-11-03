# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #[1->2->4], [1->3->5], [3->6]
        # while loop
        # check first; if lowest, move next pointer
        dummy = ListNode(0)
        curr = dummy

        while True:
            min_idx = -1 
            # find list with smallest head
            for i in range(len(lists)):
                if lists[i] is not None:
                    if min_idx == -1 or lists[i].val <       lists[min_idx].val:
                        min_idx = i
            #lists exhausted
            if min_idx == -1:
                break

            # Append the smallest node
            curr.next = lists[min_idx]
            curr = curr.next

            # Advance that list's head
            lists[min_idx] = lists[min_idx].next
        
        return dummy.next