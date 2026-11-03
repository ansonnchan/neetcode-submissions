class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums)-1

        while left < right:
            middle = left + (right+left)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                middle -=1
            else:
                middle+=1
            left+=1
            right-=1

        return -1
