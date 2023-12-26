from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []  # to store the values during traversal

        def preorder_helper(node):
            if node is not None:
                # Visit the current node
                result.append(node.val)

                # Traverse the children
                for child in node.children:
                    preorder_helper(child)

        preorder_helper(root)
        return result

# Example usage:
# Creating a simple tree
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2, [Node(4)])])

# Using the Solution class to perform pre-order traversal
solution = Solution()
result = solution.preorder(root)
print("Pre-order traversal:", result)
