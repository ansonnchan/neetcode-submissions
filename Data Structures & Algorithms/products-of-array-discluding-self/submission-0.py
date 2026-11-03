class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            curr = 1
            for j in range(len(nums)):
                if i !=j:
                    curr*=nums[j]
            res.append(curr)
        
        return res #O(n^2)