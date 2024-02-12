# Definition for a binary tree node.
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