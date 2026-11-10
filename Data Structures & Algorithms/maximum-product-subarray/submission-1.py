class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 1
        currMin = 1

        for num in nums:
            tempMax = max(num, currMax * num, currMin * num)
            currMin = min(num, currMax * num, currMin * num)

            currMax = tempMax
            res = max(res, currMax)

        return res