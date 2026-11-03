class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0 

        max_sequence=1
        for i in range(len(nums)):
            curr = 1
            num = nums[i]
            while num+1 in nums:
                curr+=1
                num+=1
            max_sequence=max(curr, max_sequence)

        return max_sequence 
        