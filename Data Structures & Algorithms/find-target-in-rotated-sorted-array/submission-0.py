class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #first thing to do is get it back to original
        #then just use binary search

        #brute force
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

        #trivial solution -> O(n), O(1)