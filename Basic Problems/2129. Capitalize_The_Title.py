class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        result_words = []

        for word in words:
            if len(word) <= 2:
                result_words.append(word.lower())
            else:
                result_words.append(word.capitalize())

        result_string = ' '.join(result_words)
        return result_string