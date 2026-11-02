class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #instead of counter, we could also consider sorting then keeping some sort of status flag; but that would be O(nlogn)

        #instead XOR gives us the property
        # x ^ x = 0 (cancels out )
        result = 0
        for num in nums:
            result ^= num
        
        return result 

        
        
        