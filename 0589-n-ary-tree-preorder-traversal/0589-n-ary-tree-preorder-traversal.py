# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


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
        