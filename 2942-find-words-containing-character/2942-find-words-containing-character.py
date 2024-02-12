class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        temp = []
        # Iterate through each word in the list
        for index, word in enumerate(words):
            if x in word:
                temp.append(index)

        return temp