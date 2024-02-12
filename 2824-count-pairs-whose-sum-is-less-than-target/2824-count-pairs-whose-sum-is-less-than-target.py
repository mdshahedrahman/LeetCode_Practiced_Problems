class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        temp = []
        counter = 0
        
        for i in range(len(nums)):
            for j in range(i):
                temp.append(nums [j] + nums [i])
                if temp[-1] < target:
                    counter = counter + 1
        
        return counter