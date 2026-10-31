class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #structure - number: index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        #O(n) space, O(n) time 

        