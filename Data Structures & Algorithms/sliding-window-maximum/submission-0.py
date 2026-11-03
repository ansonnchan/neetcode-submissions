class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #brute force 
        #2 loops - outer -> row, inner -> sliding window
        # take max at each
        res = []
        #need to first determine how many 
        i = 0 
        
        while i+k <= len(nums):
            curr_max = nums[i] #take base max to be first element in the sliding window
            for _ in range(i, i+k):
                #determine max here
                curr_max = max(curr_max, nums[_])
            
            res.append(curr_max)
            i+=1
        return res

        
