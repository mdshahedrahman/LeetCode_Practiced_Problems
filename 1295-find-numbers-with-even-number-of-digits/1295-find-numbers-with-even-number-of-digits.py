class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digit_counts = [len(str(num)) for num in nums]

        count = 0

        for i in digit_counts:
            if i % 2 == 0:
                count = count + 1

        return count