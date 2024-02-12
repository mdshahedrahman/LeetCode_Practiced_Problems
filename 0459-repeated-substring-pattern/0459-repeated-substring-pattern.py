class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)

        # Check all possible substrings up to half of the length
        for substring_length in range(1, length // 2 + 1):
            if length % substring_length == 0 and s[:substring_length] * (length // substring_length) == s:
                return True

        return False
