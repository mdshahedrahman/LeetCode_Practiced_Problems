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

# Example usage:
root_node = TreeNode(5)
root_node.left = TreeNode(3)
root_node.right = TreeNode(6)
root_node.left.left = TreeNode(2)
root_node.left.right = TreeNode(4)
root_node.left.left.left = TreeNode(1)
root_node.right.right = TreeNode(8)
root_node.right.right.left = TreeNode(7)
root_node.right.right.right = TreeNode(9)

solution = Solution()
result_tree = solution.increasingBST(root_node)

# Print the result_tree in a readable format
def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.val, end=" ")
        print_tree(node.right)

print_tree(result_tree)
