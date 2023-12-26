from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root


# Example usage:
sorted_array = [-10,-3,0,5,9]
solution = Solution()
bst_root = solution.sortedArrayToBST(sorted_array)

# Function to perform in-order traversal of the BST for verification
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

print("In-order traversal of the generated BST:")
inorder_traversal(bst_root)
