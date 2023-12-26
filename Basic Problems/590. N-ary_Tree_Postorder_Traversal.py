from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []  # to store the values during traversal

        def postorder_helper(node):
            if node is not None:
                # Traverse the children
                for child in node.children:
                    postorder_helper(child)

                # Visit the current node
                result.append(node.val)

        postorder_helper(root)
        return result

# Example usage:
# Creating a simple tree
root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2, [Node(4)])])

# Using the Solution class to perform pre-order traversal
solution = Solution()
result = solution.postorder(root)
print("Post-order traversal:", result)
