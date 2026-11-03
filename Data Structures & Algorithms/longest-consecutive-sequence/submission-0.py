class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_sequence=1
        for i in range(len(nums)):
            curr = 1
            while nums[i]+1 in nums:
                curr+=1
                nums[i]+=1
            max_sequence=max(curr, max_sequence)

            i+=curr
        return max_sequence 
        