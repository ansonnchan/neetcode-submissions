class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        target = Counter(t)
        window = {}

        left = 0
        have = 0
        need = len(target)

        shortest = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Check if this character's frequency is satisfied
            if char in target and window[char] == target[char]:
                have += 1

            # Valid window: try shrinking from the left
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    shortest = s[left:right + 1]

                # Remove leftmost character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1

                left += 1

        return shortest
            



        