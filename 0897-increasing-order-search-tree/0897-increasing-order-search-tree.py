# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)

                # Modify the original tree in-place
                self.prev.right = node
                node.left = None
                self.prev = node

                inorder_traversal(node.right)

        # Create a dummy node to simplify the code
        dummy = TreeNode()
        self.prev = dummy
        inorder_traversal(root)

        return dummy.right