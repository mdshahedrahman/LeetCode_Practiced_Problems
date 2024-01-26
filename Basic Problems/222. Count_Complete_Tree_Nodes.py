# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current_node = queue.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)

        i += 1

    return root

def count_nodes(root):
    if not root:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Given list
root_list = [1, 2, 3, 4, 5, 6]

# Construct the tree
root_node = build_tree(root_list)

# Count the number of nodes
node_count = count_nodes(root_node)

print("Number of nodes in the tree:", node_count)
