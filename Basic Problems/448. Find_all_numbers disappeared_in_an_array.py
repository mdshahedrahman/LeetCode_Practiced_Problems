nums = [4, 3, 2, 7, 8, 2, 3, 1]

# Initialize a dictionary to store counts
number_counts = {}
temp = []

# Count occurrences of each number from 1 to len(nums)
for i in range(1, len(nums) + 1):
    number_counts[i] = nums.count(i)

# Print numbers that appear 0 times
for number, count in number_counts.items():
    if count == 0:
       temp.append(number)

print(temp)
