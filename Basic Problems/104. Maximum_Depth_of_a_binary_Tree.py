from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        # The depth of the tree is the maximum depth of its left and right subtrees, plus 1 for the current node.
        return max(left_depth, right_depth) + 1

# Example usage:
# Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculating the depth of the tree using the Solution class
solution = Solution()
depth = solution.maxDepth(root)
print("Depth of the binary tree:", depth)
