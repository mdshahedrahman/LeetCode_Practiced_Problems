class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        temp = []
        temp_1 = []

        temp = [0] + gain

        sum = temp[0]

        for i in temp:
            sum = sum + i
            temp_1.append(sum)
        
        return (max(temp_1))