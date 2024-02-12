class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count_dict = {}

        # Count occurrences of each number
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        # Calculate the number of elements smaller than each element
        result = [sum(count_dict[key] for key in count_dict if key < num) for num in nums]

        return result