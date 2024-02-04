from typing import List
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        encoded = [first] + encoded

        temp = []
        temp.append(encoded[0])
        result = encoded[0]

        for i in range(len(encoded)-1):
            result = result ^ encoded[i + 1]
            temp.append(result)

        return temp