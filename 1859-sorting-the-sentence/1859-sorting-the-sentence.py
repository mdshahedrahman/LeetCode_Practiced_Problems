class Solution:
    def sortSentence(self, s: str) -> str:
        digit_word_pairs = [(int(char), word)
                    for word, char in zip(s.split(), filter(str.isdigit, s))]

        # Sort the digit-word pairs based on the digits
        sorted_digit_word_pairs = sorted(digit_word_pairs, key=lambda x: x[0])

        # Remove the last digit from each word
        modified_words = [word[:-1] for _, word in sorted_digit_word_pairs]

        # Concatenate the modified words into one string
        result_string = ' '.join(modified_words)

        # Print the result string
        return result_string