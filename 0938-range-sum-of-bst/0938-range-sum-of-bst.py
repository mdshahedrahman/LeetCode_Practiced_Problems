# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def in_order_traversal(node, result):
            if node is not None:
                in_order_traversal(node.left, result)
                result.append(node.val)
                in_order_traversal(node.right, result)

        
        sorted_nodes = []
        temp = []

        in_order_traversal(root, sorted_nodes)
          
        for i in sorted_nodes:
            if isinstance(i, int) and low <= i <= high:
                temp.append(i)

        sum_temp = sum(temp)

        return sum_temp