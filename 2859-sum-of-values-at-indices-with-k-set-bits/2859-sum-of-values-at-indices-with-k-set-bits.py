class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        temp = []
        sum_1 = 0

        for i in range(len(nums)):
            binary_representation = bin(i)[2:]
            temp.append(binary_representation)

        count_of_ones = [bin_str.count('1') for bin_str in temp]

        for i, value in enumerate(count_of_ones):
            if value == k:
                sum_1 = sum_1 + nums[i]

        return sum_1