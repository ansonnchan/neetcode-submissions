class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #a better solution is maybe doing a cycle
        #if we treat like linkedlist, we point to index
        #if multiple index, multiple will point to index
        # so there will be a cycle
        # if we detect cycle then there must be a duplicate

        #detect cycle
        slow=fast=nums[0] 
        while True:
            slow=nums[slow] 
            fast=nums[nums[fast]]
            if slow == fast:
                break
        #now our pointers are pointing to duplicate
        slow=nums[0]
        
        #the reason we can do this is because we're guaranteeded only 1 repeated 
        while slow != fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow 

        