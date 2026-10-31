class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        max_sequence = 0

        for num in num_set:
            # Only start counting at the beginning of a sequence
            if num - 1 not in num_set:
                curr = 1

                while num + curr in num_set:
                    curr += 1

                max_sequence = max(curr, max_sequence)

        return max_sequence
        