from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        temp = []
        temp.append(pref[0])
        for i in range(len(pref) - 1):
            count = pref[i] ^ pref[i + 1]
            temp.append(count)

        return temp