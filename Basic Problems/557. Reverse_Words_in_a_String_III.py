class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words
        words = s.split()

        # Swap each word
        swapped_words = [''.join(reversed(word)) for word in words]

        # Join the swapped words into a new string
        result = ' '.join(swapped_words)

        return result