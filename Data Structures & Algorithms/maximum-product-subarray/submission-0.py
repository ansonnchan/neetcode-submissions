class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #brute force two loops

        res = nums[0]
        for i in range(len(nums)):
            currentProduct = 1 
            for j in range(i, len(nums)):
                currentProduct *= nums[j]
                res=max(res,currentProduct)
        
        return res
