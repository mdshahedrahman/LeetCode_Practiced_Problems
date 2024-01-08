from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def swap_subtrees(node):
            if node is not None:
                # Swap the left and right subtrees of the current node
                node.left, node.right = node.right, node.left

                # Recursively swap the left and right subtrees of the children
                swap_subtrees(node.left)
                swap_subtrees(node.right)

        swap_subtrees(root)
        return root

    def print_tree(self, root):
        if root is None:
            return None

        # Build the binary tree using the values in the list
        queue = [TreeNode(val=root[0])]
        i = 1
        while i < len(root):
            current = queue.pop(0)
            if current is not None:
                current.left = TreeNode(val=root[i]) if root[i] is not None else None
                i += 1
                queue.append(current.left)

                if i < len(root):
                    current.right = TreeNode(val=root[i]) if root[i] is not None else None
                    i += 1
                    queue.append(current.right)

        return queue[0]