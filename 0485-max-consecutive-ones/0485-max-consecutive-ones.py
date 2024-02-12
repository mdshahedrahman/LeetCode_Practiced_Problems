class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        temp = []
        count_1 = 0

        for i in nums:
            if i == 1:
                count_1 = count_1 + 1
            else: count_1 = 0
            temp.append(count_1)

        return max(temp)