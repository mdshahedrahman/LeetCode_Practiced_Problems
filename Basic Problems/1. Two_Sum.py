from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    temp.append(i)
                    temp.append(j)
                    print(temp)
        return temp


nums = [int(x) for x in input().split()]
target = int(input("target: "))
print("nums:", nums)

solution_obj = Solution()
solution_obj.twoSum(nums, target)
