class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count_s = {}
        char_count_t = {}

        # Count occurrences in string s
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        # Count occurrences in string t
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        # Compare the dictionaries
        return char_count_s == char_count_t
