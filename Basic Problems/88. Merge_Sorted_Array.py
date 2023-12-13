nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

# Extend nums1 with nums2
nums1.extend(nums2)

# Sort the modified nums1 in-place
nums1.sort()

while nums1 and nums1[0] == 0:
    nums1.pop(0)

print(nums1)
