# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


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