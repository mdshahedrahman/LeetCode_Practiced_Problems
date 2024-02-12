class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = haystack.find(needle)

        # Check if the needle is found
        if index != -1:
            return index
        else:
            return -1
        