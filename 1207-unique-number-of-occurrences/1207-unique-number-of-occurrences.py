class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize an empty dictionary to store counts
        element_count = {}

        # Loop through the array
        for element in arr:
            # If element is already in the dictionary, increment its count
            if element in element_count:
                element_count[element] += 1
            # If element is not in the dictionary, add it with a count of 1
            else:
                element_count[element] = 1

        # Get the set of counts
        counts_set = set(element_count.values())

        # Check if counts are distinct
        if len(counts_set) == len(element_count):
            return True
        else:
            return False
