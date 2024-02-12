class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize pointers and a counter for the current element's occurrences
        slow, fast, count = 1, 1, 1

        for fast in range(1, len(nums)):
            # Check if the current element is equal to the previous one
            if nums[fast] == nums[fast - 1]:
                count += 1
            else:
                count = 1  # Reset the count for a new element

            # Copy the current element if it appears at most twice
            if count <= 2:
                nums[slow] = nums[fast]
                slow += 1

        return slow