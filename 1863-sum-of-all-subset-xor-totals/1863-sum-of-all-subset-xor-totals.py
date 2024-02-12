class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor_sum = 0

        for i in range(1 << len(nums)):
            subset = [nums[j] for j in range(len(nums)) if (i & (1 << j)) > 0]
            subset_xor = 0

            for num in subset:
                subset_xor ^= num

            total_xor_sum += subset_xor

        return total_xor_sum