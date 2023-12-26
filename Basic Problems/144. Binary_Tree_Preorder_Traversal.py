from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []  # to store the values during traversal

        def preorder_helper(node):
            if node is not None:
                # Visit the current node
                result.append(node.val)

                # Traverse the left subtree
                preorder_helper(node.left)

                # Traverse the right subtree
                preorder_helper(node.right)

        preorder_helper(root)
        return result

# Example usage:
# Creating a simple binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Using the Solution class to perform pre-order traversal
solution = Solution()
result = solution.preorderTraversal(root)
print("Pre-order traversal:", result)
