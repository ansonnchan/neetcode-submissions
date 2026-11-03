class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        #brute force solution
        #find the minimum and thats it 
        
        #what we do know is that the next element is strictly greater
        #is find the index where its minimum
        #then do binary search on that index

        # First binary search: find minimum index
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]

        