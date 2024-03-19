class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp_1 = []
        temp = { }

        for i in nums:
            if i in temp:
                temp [i] += 1
            else:
                temp [i] = 1

        sorted_counts = sorted(temp.items(), key=lambda x: x[1], reverse = True)

        for elem, count in sorted_counts[: k]:
            temp_1.append(elem)
        
        return temp_1
    