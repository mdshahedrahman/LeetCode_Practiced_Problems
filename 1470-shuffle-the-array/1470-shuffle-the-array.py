class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []

        for j in range(n):
            for i in range(j, 2*n , n):
                temp.append(nums[i])



        return temp