from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_arr = list(set(arr))
        sorted_arr = sorted(unique_arr)
        
        rank_dict = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
        
        ranks = [rank_dict[val] for val in arr]

        return ranks
