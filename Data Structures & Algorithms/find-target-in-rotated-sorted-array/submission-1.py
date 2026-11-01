class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # First binary search: find minimum index
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        rotation = left

        # Second binary search: find target
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2

            actual_index = (middle + rotation) % len(nums)

            if nums[actual_index] == target:
                return actual_index
            elif nums[actual_index] < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1