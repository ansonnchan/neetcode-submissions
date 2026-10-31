class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left, right = 0, 0
        freq = {}

        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1

            max_freq = max(freq.values())

            while (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                max_freq = max(freq.values())

            longest = max(longest, right - left + 1)
            right += 1

        return longest