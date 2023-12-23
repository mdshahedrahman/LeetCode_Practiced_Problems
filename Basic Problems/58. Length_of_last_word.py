class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_sentence = s.rstrip(".,?!")

        # Split the sentence into words
        words = cleaned_sentence.split()

        # Check if there are any words in the sentence
        if words:
            # Extract the last word
            last_word = words[-1]
            result = len(last_word)
            return result

