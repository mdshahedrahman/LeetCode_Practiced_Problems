from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = list(set(arr))
        sorted_arr = sorted(unique_arr)
        temp = []

        for i in range(len(arr)):
            for j in sorted_arr:
                if arr[i] == j:
                    k = sorted_arr.index(j) + 1
                    temp.append(k)

        return temp